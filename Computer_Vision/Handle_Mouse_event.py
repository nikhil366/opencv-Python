import cv2
import numpy

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image = cv2.imread(image_path)

def click_event_mouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)
        font = cv2.FONT_HERSHEY_PLAIN
        strxy = str(x) + ' , ' + str(y)
        cv2.putText(image,strxy, (x,y), font,1,(255,0,124),2, cv2.LINE_AA)
        cv2.imshow('image', image)

cv2.imshow('image',image)

cv2.setMouseCallback('image', click_event_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
        