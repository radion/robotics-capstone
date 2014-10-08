#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

bumps = False

def callback(data):
    global bumps
    # print data
    # print data.bumper

    if data.bumper == 1:
        bumps = not bumps
        print "bump"

def talker():
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    bumper = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.5
        global bumps
        if bumps:
            twist.linear.x = -0.5
            bumps = not bumps
        pub.publish(twist)
        r.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
