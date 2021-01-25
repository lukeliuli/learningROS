#!/usr/bin/env python

import rospy
from rospy.numpy_msg import numpy_msg
from numpy_test1.msg import myMsg1

import numpy
def talker():
    pub = rospy.Publisher('myMsg1', numpy_msg(myMsg1),queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        a = numpy.array([1.0, 2.1, 3.2, 4.3, 5.4, 6.5], dtype=numpy.float32)
        pub.publish(a)
        r.sleep()

if __name__ == '__main__':
    talker()
