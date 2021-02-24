'''Image Pyramid
Basically when we use images we use images of constant size but some times we have to use images 
of diffrent size or diffrent resolution so for that we use image Pyramid
let's take an example we have several images of diffrent resolution and we just want to detect 
face in the images then we can detect the faces with the help of image_Pyramid_opencv  
Image Pyramid are of two types :
1. gaussian Pyramid
 gaussian Pyramid  - repeat filtering and sub sampling of image

2. Laplacian Pyramid
'''

# Gaussian Pyramid - gaussian Pyramid work on two factoe PyrDown(for decrease resolution)
#  and PyrUp(for increase resolution)

import cv2
import numpy as np

image_path = ('/home/nikhil/Desktop/Data/nik.jpeg')
image = cv2.imread(image_path)

pyrdown = cv2.pyrDown(image)
pyrdown1 = cv2.pyrDown(pyrdown)
pyrup = cv2.pyrUp(image)

while True:
    cv2.imshow('image',image)
    cv2.imshow('pyrdown_image',pyrdown) # reduce resolution of the image
    cv2.imshow('pyrdown_image1',pyrdown1) # reduce resolution of the image pyrdown
    cv2.imshow('pyrup_image',pyrup) # for increase the resolution
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()