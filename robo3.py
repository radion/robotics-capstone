#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField

# This callback is called when the Kinect Sensor gives back readings
def callback(data):
    data_out = pc2.read_points(data)
    int_data = next(data_out)
    int_data1 = next(data_out)

    depth = int_data[2]
    x = int_data[0]
    y = int_data[1]
    #print len(int_data)
    rospy.loginfo("1: " + str(int_data));
    rospy.loginfo("2: " + str(int_data1));
    rospy.loginfo(" ");
    # rospy.loginfo("depth: " + str(depth) + ", x: " + str(x) + ", y: " + str(y) + " last " + str(int_data[3]))

    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    r = rospy.Rate(10) # 10hz
    twist = Twist()
    twist.linear.x = 0.5


    if math.isnan(depth):
        print 'not close'
    elif depth < 1.0:
        twist.linear.x = 0.0

    # pub.publish(twist)
    r.sleep()
   
    # To control the velocity of the mobile base based on the values from the Kinect Sensor
    
def listener():
    # Reading x, y & z data from the Kinect Sensor
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/camera/depth/points", PointCloud2, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()