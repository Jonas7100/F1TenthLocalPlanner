#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from rosgraph_msgs.msg import Clock

clkmsg = None
	
def callback(data):
    rospy.loginfo(data.header.stamp)
    rospy.loginfo(clkmsg)


def callbackClock(data):
    global clkmsg
    clkmsg = data

def listener():
    rospy.init_node('timeLidarPrinter',anonymous=True)
    rospy.Subscriber('scan', LaserScan, callback)
    rospy.Subscriber('clock', Clock, callbackClock)
    rospy.spin()

if __name__ == '__main__':
    listener()
