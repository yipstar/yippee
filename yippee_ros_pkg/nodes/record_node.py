#!/usr/bin/env python

import rospy

from std_msgs.msg import Bool
from mavros_msgs.msg import RCIn

record_state = "off"
pub = None

def callback(msg):
    global record_state, pub

    # print msg.channels
    record_channel = 5

    print msg.channels[record_channel]

    do_record_pwm = 2006

    if msg.channels[record_channel] == do_record_pwm:
        if record_state == "off":
            print "Start recording..."
            record_state = "on"
            pub.publish(True)
        else:
            print "already recording"
    else:
        if record_state == "on":
            record_state = "off"
            print "Stopping recording."
            pub.publish(False)



rospy.init_node('recorder_node')

pub = rospy.Publisher('/meka/rosbagremote/record', Bool, queue_size=1)

sub = rospy.Subscriber('/mavros_node/rc/in', RCIn, callback)

rospy.spin()

# rate = rospy.Rate(2)
# while not rospy.is_shutdown():
#     # pub.publish()
#     rate.sleep()


