#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import radians

def move():

	rospy.init_node('turtlesim_node', anonymous=True)
	V_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_cmd = Twist()
	vel_cmd.linear.x = 0.2
	vel_cmd.angular.z = 0

	timestart = rospy.Time.now()
	rate = rospy.Rate(5)

	turn_cmd = Twist()
	turn_cmd.linear.x = 0.0
	turn_cmd.angular.z = radians(45)
	count = 0
	while not rospy.is_shutdown():
		for x in range(0,10):
			V_publisher.publish(vel_cmd)
			rate.sleep()
		for x in range (0,10):
			V_publisher.publish(turn_cmd)
			rate.sleep()
		count = count +1
		if (count == 4):
			count = 0
		if (count == 0):
			rospy.loginfo("Turtle Complete")

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass

