#!/usr/bin/env python
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
import os
import cv2
import numpy as np
import time
IMAGE_WIDTH=200
IMAGE_HEIGHT=200

#
#using rqt_image_view or 
#http://wiki.ros.org/image_view
# rosrun imageview
#rosrun image_view image_view image:=/image/CompressedImage theora
#rosrun image_view image_view image:=/image/CompressedImage image_transport:='compressed'

def read_pub():
    rospy.init_node("testImage", anonymous=True)
    

    #########################################################################
    #pub raw
    image_publish=rospy.Publisher('/image/image_raw',Image,queue_size=1)
    
    imagedata = cv2.imread('/home/ros1/testImages/1.jpg')

    image_temp=Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_temp.height=IMAGE_HEIGHT
    image_temp.width=IMAGE_WIDTH
    image_temp.encoding='rgb8'
    image_temp.data=np.array(imagedata).tostring()
    image_temp.header=header
    image_temp.step=IMAGE_WIDTH*3
    image_publish.publish(image_temp)
    rospy.loginfo("pub 1 raw")


       
    ########################################################################### 
    #pub jpeg don't work,python dont support image transport
    
    #imagecomress_pubulish=rospy.Publisher('/image/CompressedImage',CompressedImage,queue_size=1)
    #imagedata2 = cv2.imread('/home/ros1/testImages/2.bmp')

    #img_encode = cv2.imencode('.jpg', imagedata2)[1]
    #data_encode = np.array(img_encode)
    #str_encode = data_encode.tostring()

    #imageCompressed = CompressedImage()
    #imageCompressed.header.stamp = rospy.Time.now()
    #imageCompressed.format = "jpeg"
    #imageCompressed.data = str_encode
    #imagecomress_pubulish.publish(imageCompressed)
    #rospy.loginfo("pub 2 jpeg")
    
    ########################################################################### 
    #pub jpeg don't work,python dont support image transport
    cvcap_publish=rospy.Publisher('/image/cvcap',Image,queue_size=1)

    videoSrc = '/home/ros1/testImages/1.mp4'
    cap = cv2.VideoCapture(videoSrc)
    rval, frame = cap.read()
    image_cap=Image()
    header = Header(stamp=rospy.Time.now())
    header.frame_id = 'map'
    image_cap.height=960
    image_cap.width=544
    image_cap.encoding='rgb8'
    image_cap.data=np.array(frame).tostring()
    image_cap.header=header
    image_cap.step=544*3
    cvcap_publish.publish(image_cap)

    ########################################################################### 
    jpeg_pubulish=rospy.Publisher('/image/JPGImage',CompressedImage,queue_size=1)
    bmpImg = cv2.imread('/home/ros1/testImages/2.bmp')

    img_encode = cv2.imencode('.jpg', bmpImg)[1]
    data_encode = np.array(img_encode)
    str_encode = data_encode.tostring()

    imageCompressed = CompressedImage()
    imageCompressed.header.stamp = rospy.Time.now()
    imageCompressed.format = "jpeg"
    imageCompressed.data = str_encode
    jpeg_pubulish.publish(imageCompressed)
    rospy.loginfo("pub 4 jpeg")

    rate = rospy.Rate(0.1) # 2hz
    while not rospy.is_shutdown():

        image_temp.header.stamp = rospy.Time.now()
        image_publish.publish(image_temp)
        rospy.loginfo("pub 1 image raw")
        rate.sleep()

        imageCompressed.header.stamp = rospy.Time.now()
        jpeg_pubulish.publish(imageCompressed)
        rospy.loginfo("pub 4 jpeg")
        rate.sleep()

        rval, frame = cap.read()
        image_cap.header.stamp = rospy.Time.now()
        image_cap.data=np.array(frame).tostring()
        cvcap_publish.publish(image_cap) 
        rospy.loginfo("pub 3 cvCap")
        rate.sleep()
          
   
if __name__ == '__main__':
    read_pub()

