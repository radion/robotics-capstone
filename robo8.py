#!/usr/bin/env python

# Goes to marker that was clicked on

import roslib;
import rospy
import actionlib

#move_base_msgs
from move_base_msgs.msg import *
from visualization_msgs.msg import Marker
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from visualization_msgs.msg import InteractiveMarkerFeedback

def callback(data):
	# print data.pose.position.x
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
	if data.id == 7:
		twist = Twist()
		if data.pose.position.x > 0.05 or data.pose.position.x < -0.05:
			twist.angular.z = -1 * 6 * data.pose.position.x
		else:
			if data.pose.position.z > 0.2:
				twist.linear.x = 0.2
			else:
				twist.linear.x = 0
		pub.publish(twist)
	

def simple_move():
    rospy.init_node('listener', anonymous=True) 
    rospy.Subscriber('/visualization_marker', Marker, callback)
    rospy.spin()

if __name__ == '__main__':
    simple_move()
    