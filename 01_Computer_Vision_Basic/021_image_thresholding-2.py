'''
so here we will discuss about image thresholding on a image.
image in a black and white colour image and we will see in this
how a image threshold affect a image.

there are sevral types of image thresholding we will see one by one

2. IMAGE Thresholding  - THRESH_BINARY_INVERSE
THRESH_BINARY_INVERSE - is use to inverse the result of binary image.

3. IMAGE Thresholding  - THRESH_TRUNK
THRESH_TRUNK - here thresh trunk pixel is use to set the minimum pixel
value to the end of pixel we use this for example you can see where we 
apply threshtrunk thresh level 127 from 127 pixel whole image pixel
is like 127.
'''

import cv2
import numpy as np

image_path = ('/home/nikhil/Desktop/Data/Black_white_image.jpg')
image = cv2.imread(image_path,0)


while(True):
    ret1, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV )
    ret2, th2 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
    ret3, th3 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
    print(ret1)
    print(th1)

    cv2.imshow('TH3', th3)
    cv2.imshow('TH2', th2)
    cv2.imshow('TH1',th1)
    cv2.imshow('threshold_image',image)
    k = cv2.waitKey(0)  & 0xFF
    if k == 27:
        break 