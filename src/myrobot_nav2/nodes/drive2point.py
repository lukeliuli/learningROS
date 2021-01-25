#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
from nav_msgs.msg import Odometry
from geometry_msgs.msg import *

desX = 10
desY = 10
desTheta = 90/180*3.1415
global mycmd_vel 

def handle_odom_pose(odom_data):

	curr_time = odom_data.header.stamp
	pose = odom_data.pose.pose
	orient = odom_data.pose.pose.orientation
	pos = pose.position
	x= pos.x
	y= pos.y
	(roll, pitch, theta) = tf.transformations.euler_from_quaternion([orient.x, orient.y, orient.z, orient.w])
	angle_to_goal = math.atan2(desY-y, desX-x)

	if abs(angle_to_goal - theta) > 10*3.14/180:
		speed= 0.0
		angular= 0.3
	else:
		angular= 0.0
		speed =0.2

	cmd = geometry_msgs.msg.Twist()
	cmd.linear.x = speed
	cmd.angular.z = angular
	mycmd_vel.publish(cmd)
	rospy.loginfo('send cmd_vel')


if __name__ == '__main__':
    rospy.init_node('drive2point',anonymous=True)
    mycmd_vel = rospy.Publisher('/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)
    
    rospy.Subscriber("odom", Odometry, handle_odom_pose)
    rospy.spin()

