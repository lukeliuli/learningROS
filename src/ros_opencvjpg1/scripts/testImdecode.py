#!/usr/bin/env python


import os
import cv2
import numpy as np
import time
import random



def testImdecode1():
    data1 = np.zeros([120000,1],dtype=np.uint8);
    img_decode = cv2.imdecode(data1, cv2.IMREAD_COLOR )
    str1 = '/home/ros1/tmpImages/test'+str(1000)+'.png'
    cv2.imwrite(str1, img_decode)

if __name__ == '__main__':
    testImdecode1()
