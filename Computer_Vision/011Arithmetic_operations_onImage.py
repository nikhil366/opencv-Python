'''here we are goingto  understandho we cansplit a image on the basis 
of there channel. here in this code we are going to split the image in 
b,g,r we can split image with the help of functions call shape,size,dtype, split 
and we can merge back with the help of merge '''

import cv2

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image_load = cv2.imread(image_path)

'''here we use some function to know some information about image'''

print(image_load.shape) # return number of row and column and chanel in tupple 
print(image_load.size)  # return total number of pixel is accessed
print(image_load.dtype) # return image data type is obtained
b,g,r = cv2.split(image_load)
# print((b,g,r))
image_load = cv2.merge((b,g,r))
print(image_load.shape)
print(image_load.size)
print(image_load.dtype)

cv2.imshow('image',image_load)
cv2.waitKey(0)
cv2.destroyAllWindows()