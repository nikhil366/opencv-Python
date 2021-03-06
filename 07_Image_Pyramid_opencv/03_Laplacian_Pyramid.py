'''Here we Discuss about Laplacian Pyramid in Gaussian Pyramid we have 
predefine Functions to increase and decrease the resolution but in laplacian 
Pyramid we dont have any function for image conversion.
In Laplacian Pyramid the result we got in the form of edge detection,
result you will see in this code '''


import cv2
import numpy as np

image_path = ('/home/nikhil/Desktop/Data/lena.png')
img = cv2.imread(image_path)

layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)
    #cv2.imshow(str(i), layer)

layer = gaussian_pyramid_list[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()