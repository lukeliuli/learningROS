#!/usr/bin/env python

from __future__ import print_function

from beginner1.srv import AddTwoInts,AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
   # print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
   print("running handle_add_two_ints")
   sum = req.A+req.B
   return AddTwoIntsResponse(sum)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
