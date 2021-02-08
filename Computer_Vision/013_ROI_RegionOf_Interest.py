'''here in this section we are going to work on ROI of image ROI is stands for
Region of interest. in this section we will uderstand how we can extract those
parts of image which we need for our data. Here in this Most role of numpy 
indexing feature'''
import cv2
import numpy as np

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image_load = cv2.imread(image_path)

'''here we use some function to know some information about image'''

print(image_load.shape) # return number of row and column and chanel in tupple 
print(image_load.size)  # return total number of pixel is accessed
print(image_load.dtype) # return image data type is obtained
b,g,r = cv2.split(image_load)
# print((b,g,r))
image_load = cv2.merge((b,g,r))

face = image_load[50:250, 150:550]



'''
The co-ordinates used in the array follow the format of 
img [y1: y2, x1: x2]
Therefore, when copying to another part of the image, you need to ensure that (y2-y1) value remains the same, as well as (x2-x1)

Here's another example to copy messi's head, where Top left coordinates is (200, 60) and bottom right is (270, 140) in x,y format

messi_head = img[60:140, 200:270]
img[260:340,100:170] = messi_head
'''




cv2.imshow('image',face)
cv2.waitKey(0)
cv2.destroyAllWindows()