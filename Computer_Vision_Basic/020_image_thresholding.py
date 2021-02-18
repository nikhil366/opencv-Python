'''
so here we will discuss about image thresholding on a image.
image in a black and white colour image and we will see in this
how a image threshold affect a image.

there are sevral types of image thresholding we will see one by one

1. Simple thresholding (Binary Thresholding)
Binary thresholding is the way where result is declare in 2 forms
either in 0 or in 1
if pixel = 0(zero) then it will black
if pixel = 255 - white
'''



import cv2
import numpy as np

image_path = ('/home/nikhil/Desktop/Data/Black_white_image.jpg')
image = cv2.imread(image_path,0)

'''
here in this we will see a image which move from black to white in 
left to right direction.
- colour intensity on balck side is closer to zero
- colour intensity on white side is closer to 255
'''

while(True):
    ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY )
    print(ret)
    print(th1)
    cv2.imshow('TH1',th1)
    cv2.imshow('threshold_image',image)
    k = cv2.waitKey(0)  & 0xFF
    if k == 27:
        break 