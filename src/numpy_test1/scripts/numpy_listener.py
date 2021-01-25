#!/usr/bin/env python

import rospy
from numpy_test1.msg import myMsg1
from rospy.numpy_msg import numpy_msg

def callback(data):
   
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():
    rospy.init_node('listener')
    #rospy.Subscriber("myMsg1", myMsg1, callback)
    rospy.Subscriber("myMsg1", numpy_msg(myMsg1), callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
