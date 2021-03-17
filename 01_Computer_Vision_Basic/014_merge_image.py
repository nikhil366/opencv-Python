'''here in this you will learn how to resize 
a picture as well as after resize how to merge 
two  picture in one image and how we can apply weight
which picture is going to more visible'''


import cv2
import numpy as np

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image_path_2 = "/home/nikhil/Pictures/ni.jpg"


image = cv2.imread(image_path)
image2 = cv2.imread(image_path_2)

resize_image = cv2.resize(image, (512,512))
resize_image2 = cv2.resize(image2, (512,512))


#cv2.add(resize_image, resize_image2)

'''for add weight in images there is formula for that this formula is 
[dst = image1*alpha + image2*beta + gamma]
so basically this is formula for add weight in images'''
new_image = cv2.addWeighted(resize_image, .5, resize_image2, .5, 0);

# face = image[50:250, 150:550]
# print(face.shape)

#cv2.imshow('resize_image',resize_image)
# cv2.imshow('image',face)
cv2.imshow('merge_image',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()