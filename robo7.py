#!/usr/bin/env python

# Goes to marker that was clicked on

import roslib;
import rospy
import actionlib

#move_base_msgs
from move_base_msgs.msg import *
from visualization_msgs.msg import Marker
from std_msgs.msg import String
from visualization_msgs.msg import InteractiveMarkerFeedback

def callback(data):
	if data.mouse_point_valid and data.event_type == 5:
	    #Simple Action Client
	    sac = actionlib.SimpleActionClient('/move_base', MoveBaseAction )

	    #create goal
	    goal = MoveBaseGoal()
	    #set goal
	    goal.target_pose.pose.position.x = data.pose.position.x
	    goal.target_pose.pose.position.y = data.pose.position.y
	    goal.target_pose.pose.orientation.w = 1.0
	    goal.target_pose.header.frame_id = 'map'
	    goal.target_pose.header.stamp = rospy.Time.now()
	    #start listner
	    sac.wait_for_server()
	    #send goal
	    sac.send_goal(goal)
	    #finish
	    sac.wait_for_result()

def simple_move():
    rospy.init_node('listener', anonymous=True) 
    rospy.Subscriber('/simple_marker/feedback', InteractiveMarkerFeedback, callback)
    rospy.spin()

if __name__ == '__main__':
    simple_move()