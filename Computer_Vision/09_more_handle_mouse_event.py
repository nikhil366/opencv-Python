'''In this file you will study about how  we can dran a line point by point using 
line function of cv2 with the help of  EVENT_LBUTTONDOWN , setMouseCallback'''
import cv2
import numpy as np


image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image = cv2.imread(image_path)
point = []
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x, y), 3, (0,0,255), -1)
        point.append((x, y ))
        print(point)
        if len(point) >= 2:
            cv2.line(image,point[-1], point[-2], (255,0,0), 5)
        cv2.imshow('image', image)
        print(point)

cv2.imshow('image',image)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()