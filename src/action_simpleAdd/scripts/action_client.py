#! /usr/bin/env python

import roslib
import rospy

import actionlib

from action_simpleAdd.msg import demoActionAction,demoActionGoal

def active_callback():
    rospy.loginfo("goal active")

def done_callback(state,res):
    rospy.loginfo(state)	
    rospy.loginfo("finish:%d",int(res.finsh))

def feedback_callback(fb):
     rospy.loginfo("percent:%f %%",fb.complete_percent)	


      
if __name__ == '__main__':
    rospy.init_node('actionclient_add')
    client =actionlib.SimpleActionClient('/simple_add',demoActionAction)
  
    client.wait_for_server()
    goal = demoActionGoal()
    goal.goal_num = 100
    client.send_goal(goal,done_callback,active_callback,feedback_callback)
    rospy.spin()

