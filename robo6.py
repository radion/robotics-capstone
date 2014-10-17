#!/usr/bin/env python
import rospy
import sys
import math
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *
from tf.msg import *
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Quaternion, Pose, Point, Vector3
from std_msgs.msg import Header, ColorRGBA

counter = 0

def callback(odom_data):
	global counter
	curr_time = odom_data.header.stamp
	pose = odom_data.pose.pose #  the x,y,z pose and quaternion orientation
	
	# print counter, curr_time
	# # print
	# print pose
	# print counter
	if counter == 0:
		print pose
	counter= counter + 1
	pub = rospy.Publisher('visualization_marker', Marker)
	marker = Marker(type=Marker.SPHERE, id=counter,
		lifetime=rospy.Duration(15),
		pose=pose,#Pose(Point(-0.5, 0.0, 0.0), Quaternion(1, 1, 1, 1)),
		scale=Vector3(0.06, 0.06, 0.06),
		header=Header(frame_id='odom'),
		color=ColorRGBA(0.0, 1.0, 0.0, 0.8))
	pub.publish(marker)
    
def listener():
    rospy.init_node('listener', anonymous=True) 
    rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

# http://answers.ros.org/question/10697/how-to-subscribe-to-odom-properly-in-python/