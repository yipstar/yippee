#!/bin/bash
gst-launch-1.0 nvcamerasrc ! 'video/x-raw(memory:NVMM), width=1920, height=(int)1080, format=(string)I420, framerate=(fraction)30/1' ! nvvidconv flip-method=0 ! 'video/x-raw, format=(string)BGRx' ! videoconvert ! 'video/x-raw, format=(string)BGR' ! nveglglessink -e

