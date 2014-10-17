#!/usr/bin/env python
import rospy
from geometry_msgs.msg import *
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
import tf
# import sys
import math
# from geometry_msgs.msg import Twist
# from geometry_msgs.msg import Twist
# import sensor_msgs.point_cloud2 as pc2
# from sensor_msgs.msg import PointCloud2, PointField
# from nav_msgs.msg import Odometry
# from geometry_msgs.msg import robot_pose_ekf
# from tf.msg import *
# from visualization_msgs.msg import Marker
# from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
# from std_msgs.msg import Header, ColorRGBA
# counter = 0

def callback(odom_data):
	#print odom_data
	# global counter
	# curr_time = odom_data.header.stamp
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
	# print euler
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
	# print deltaX
	# print deltaY

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
			
			# print "wrong quadrant"
		else:
			variable = yaw + angle
			if variable > 1.3 and variable < 1.7:
				print "pointing to origin"
				cmd.linear.x = .3
			else:
				cmd.linear.x = 0
				cmd.angular.z = .2
		# print variable
		# print angle
		# print yaw
		print yaw + angle

	turtle_vel.publish(cmd)
	# print

	# listener = tf.TransformListener()
	# (trans,rot) = listener.lookupTransform('/map', '/odom', rospy.Time(0))
	

	
	# angular = 4 * math.atan2(trans[1], trans[0])
	# linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
	
	
	# cmd.angular.z = angular
	
	# print cmd

	# rate = rospy.Rate(10.0)
	# rate.sleep()

	# # print counter, curr_time
	# # # print
	# # print pose
	# # print counter
	# if counter == 0:
	# 	print pose
	# counter= counter + 1
	# pub = rospy.Publisher('visualization_marker', Marker)
	# marker = Marker(type=Marker.SPHERE, id=counter,
	# 	lifetime=rospy.Duration(15),
	# 	pose=pose,#Pose(Point(-0.5, 0.0, 0.0), Quaternion(1, 1, 1, 1)),
	# 	scale=Vector3(0.06, 0.06, 0.06),
	# 	header=Header(frame_id='odom'),
	# 	color=ColorRGBA(0.0, 1.0, 0.0, 0.8))
	# pub.publish(marker)
    
def listener():
    rospy.init_node('listener', anonymous=True) 
    rospy.Subscriber('/robot_pose_ekf/odom_combined', PoseWithCovarianceStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

# http://answers.ros.org/question/10697/how-to-subscribe-to-odom-properly-in-python/