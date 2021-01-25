#! /usr/bin/env python

import roslib
import rospy

import actionlib

from action_simpleAdd.msg import demoActionAction,demoActionFeedback,demoActionResult

class actionServerAdd(object):
  

  def __init__(self):
   
      self.server = actionlib.SimpleActionServer('/simple_add', demoActionAction, self.execute_cb, False)
      self.server.start()
    
  def execute_cb(self, goal):
     
     i = 0
     res =demoActionResult()
     percent = demoActionFeedback()
    
     rate =rospy.Rate(0.2)
     while i < goal.goal_num:
           i=i+1
           percent.complete_percent = i/float(goal.goal_num)*100
           self.server.publish_feedback(percent)
           rate.sleep()
     
     res.finsh = True
     self.server.set_succeeded(res)      


      
if __name__ == '__main__':
    rospy.init_node('actionserver_add')
    server= actionServerAdd()
    rospy.spin() 


