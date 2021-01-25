#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner1.srv import *

def add_two_ints_client(x, y):

   
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.Sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))


    global_param = rospy.get_param("/global_param")
    print("param:global_example: %s" %global_param)
    
    # fetch the utterance parameter from our parent namespace
    foo1= rospy.get_param('/foo/foo1')
    print("param:/foo/foo1: %s" %foo1)
    
    foo2= rospy.get_param('/foo/foo2')
    print("param:/foo/fool2: %s" %foo2)

    gains = rospy.get_param('/foo/gains')
    p, i, d = gains['P'], gains['I'], gains['D']
    print("param:/foo/gains are %s, %s, %s" %(p, i, d))    
   
    topic_name = rospy.get_param('/foo/server/topic_name')
    print("param:/foo/server/topic_name %s" %topic_name)    

