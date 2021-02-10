'''here in this we will perform object detection using HSV color space
here HSV means [ Hue, Saturation, Value ]
here in this we will simply identify blue color of ball'''

import cv2
import numpy as np
from numpy.core.fromnumeric import resize
from numpy.lib.type_check import imag
image_path = ("/home/nikhil/Desktop/colorball.jpg")


# cv2.namedWindow('color')

while True:
    image_ball = cv2.imread(image_path)
    cv2.imshow('image',image_ball)
    HSV_Cnvrt_img = cv2.cvtColor(image_ball, cv2.COLOR_BGR2HSV)

    lower_limit_blue_color = np.array([110, 50, 50])
    higher_limit_blue_color = np.array([130, 250, 250])
    mask = cv2.inRange(HSV_Cnvrt_img,lower_limit_blue_color,higher_limit_blue_color)

    res = cv2.bitwise_and(image_ball,image_ball,mask=mask)

    cv2.imshow('HSV_image',HSV_Cnvrt_img)
    cv2.imshow('mask_image',mask)
    cv2.imshow('mask_image_test',res)
    k = cv2.waitKey(0)
    if k == 27:
        break

cv2.destroyAllWindows()