#!/usr/bin/env python



import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from visualization_msgs.msg import Marker
from math import radians, pi


if __name__ == '__main__':

        rospy.init_node('nav_test', anonymous=False)
        
        #############################################################################
        dist = 5 # meters
        angle = pi/2
        q_angle = quaternion_from_euler(0, 0, angle, axes='sxyz')
        q = Quaternion(*q_angle)
        target_pt = Pose(Point(dist, 0.0, 0.0), q)

        #############################################################################
        move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction) 
        # Wait 60 seconds for the action server to become available
        move_base.wait_for_server(rospy.Duration(60))
        goal = MoveBaseGoal()

		# Use the map frame to define goal poses
        goal.target_pose.header.frame_id = 'map'

		# Set the time stamp to "now"
        goal.target_pose.header.stamp = rospy.Time.now()

		# Set the goal pose to the i-th waypoint
        goal.target_pose.pose = target_pt 

        ##############################################################
        move_base.send_goal(goal)
            
        finished_within_time = move_base.wait_for_result(rospy.Duration(60)) 
            
        # If we don't get there in time, abort the goal
        if not finished_within_time:
            self.move_base.cancel_goal()
            rospy.loginfo("Timed out achieving goal")
        else:
            # We made it!
            state = self.move_base.get_state()
            if state == GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal succeeded!")


