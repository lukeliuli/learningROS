#!/usr/bin/env python


import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
import os
import cv2
import numpy as np
import time
import random
from cv_bridge import CvBridge

def callback1(image_temp):
    
       
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image_temp)
    tmpNum = random.randint(1,10000000)	
    str1 = '/home/ros1/tmpImages/test'+str(tmpNum)+'.jpg'
    cv2.imwrite(str1, cv_image) 
    return

def callback2(image_temp):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image_temp)
    tmpNum = random.randint(1,10000000)	
    str1 = '/home/ros1/tmpImages/testCap'+str(tmpNum)+'.jpg'
    cv2.imwrite(str1, cv_image) 
    return


def callback3(image_temp):
       
    

    data1=np.fromstring(image_temp.data, np.uint8)
    tmpNum = random.randint(1,10000000)	
    img_decode = cv2.imdecode(data1, cv2.IMREAD_COLOR )
    str1 = '/home/ros1/tmpImages/testJPG'+str(tmpNum)+'.jpg'
    cv2.imwrite(str1, img_decode)
    

def listener():
    #rospy.loginfo(rospy.get_caller_id() + ' data.format:', data.format)
    
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/image/image_raw', Image, callback1)
    rospy.Subscriber('/image/cvcap', Image, callback2)
    rospy.Subscriber('/image/JPGImage', CompressedImage, callback3)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
