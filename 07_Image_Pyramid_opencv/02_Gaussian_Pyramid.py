'''So here we apply Pyrdown method with for loop and we using for loop to create a Pyramid of image
and we can use for loop for create a range of pyramid.'''
import cv2
import numpy as np

image_path = ('/home/nikhil/Desktop/Data/nik.jpeg')
image = cv2.imread(image_path)

layer = image.copy()
Gaussian_Pyrmid = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    Gaussian_Pyrmid.append(layer)
    cv2.imshow(str(i), layer)    

while True:
    cv2.imshow('image',image)
    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()