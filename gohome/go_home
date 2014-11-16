#!/usr/bin/env python
import rospy
from geometry_msgs.msg import *
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
import tf
import math


def callback(odom_data):
	print "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
	pose = odom_data.pose.pose #  the x,y,z pose and quaternion orientation
	
	quaternion = (
	    pose.orientation.x,
	    pose.orientation.y,
	    pose.orientation.z,
	    pose.orientation.w)
	euler = euler_from_quaternion(quaternion)
	roll = euler[0]
	pitch = euler[1]
	yaw = euler[2]

	print "cur",
	print pose
	print
	poseO=Pose(Point(0.0, 0.0, 0.0), Quaternion(0, 0, 0, 0))
	print "0",
	print poseO
	print 

	turtle_vel = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
	cmd = geometry_msgs.msg.Twist()

	deltaY = 0 - pose.position.y
	deltaX = 0 - pose.position.x

	if abs(pose.position.x) + abs(pose.position.y) < .2:
		cmd.linear.x = 0
		cmd.angular.z = 0
		print "radion is done"
	else:
		angle = math.atan2(deltaX, deltaY)
		if angle < 0 and yaw < 0:
			variable = yaw + angle
			if variable < -3.9 and variable > -4.9:
				print "pointing to origin wrong q"
				cmd.linear.x = .3
			else:
				cmd.linear.x = 0
				cmd.angular.z = .2
		else:
			variable = yaw + angle
			if variable > 1.3 and variable < 1.7:
				print "pointing to origin"
				cmd.linear.x = .3
			else:
				cmd.linear.x = 0
				cmd.angular.z = .2
		print yaw + angle

	turtle_vel.publish(cmd)
	
    
def listener():
	print "HHHHHHHHHHHHHHH"
    rospy.init_node('listener', anonymous=True) 
    rospy.Subscriber('/beginner_tutorials/go_home_node', PoseWithCovarianceStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
