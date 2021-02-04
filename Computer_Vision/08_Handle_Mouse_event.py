'''In this Python file you can unnderstand about mouse call back function and all 
about mouse event and to completly understand this 1st you have to saw check_dir_files.py
file in this repo.'''

import cv2
import numpy

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image = cv2.imread(image_path)
    
def click_event_mouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_PLAIN
        strxy = str(x) + ' , ' + str(y)
        cv2.putText(image,strxy, (x,y), font,1,(255,0,124),1, cv2.LINE_AA)
        cv2.imshow('image', image)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = image[x, y, 0] 
        green = image[x, y, 1]
        red = image[x, y, 2]   
        font = cv2.FONT_HERSHEY_PLAIN
        strbgr = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(image,strbgr, (x,y), font,1,(255,0,124),1, cv2.LINE_AA)
        cv2.imshow('image', image)  

cv2.imshow('image',image)

cv2.setMouseCallback('image', click_event_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
        