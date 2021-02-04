import cv2
import numpy as np
from numpy.lib.type_check import imag

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"

image = cv2.imread(image_path, 1)

'''for draw a line on image'''
line_on_image = cv2.line(image,(0,0), (255,255), (255,0,0), 2)
'''for draw a arrow line on image'''
arrow_on_image = cv2.arrowedLine(image,(0,255),(255,255),(0,0,255), 4)
'''for draw a rectangle on image'''
rectangle_on_image = cv2.rectangle(image,(380,0),(510,128),(0,0,255),-1)
'''draw a circle on image'''
circle_on_image = cv2.circle(image,(447,63),63,(255,0,255),-1)
'''put text on image'''
font = cv2.FONT_HERSHEY_PLAIN
put_text_on_image = cv2.putText(image,'welcome in opencv', (23,374),font, 3, (255,255,0), 5, cv2.LINE_AA)

cv2.imshow('image_show', image)

cv2.waitKey(0)
cv2.destroyAllWindows()