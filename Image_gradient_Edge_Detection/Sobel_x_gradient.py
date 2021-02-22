'''Here in this we will discuss about Sobel_x Gradient'''


import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.type_check import imag

image_path = ('/home/nikhil/Desktop/Data/ni.jpg')
image = cv2.imread(image_path, 0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# laplacian
lap = cv2.Laplacian(image, cv2.CV_64F, ksize=5)
# just a data type 64bit float and use for transforming image from white to black
# and it deals with negative number in our image
lap = np.uint8(np.abs(lap))

# Sobel_X

sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobel_x = np.uint8(np.abs(sobel_x))
# here we can pass either one or zero because one is for show image and zero for dont show image

# Sobel_Y

sobel_y = cv2.Sobel(image, cv2.CV_64F,0,1 )
sobel_y = np.uint8(abs(sobel_y))


# sobel Combine
# we can also do sobel combine means we can combine image of x sobel and as well as y sobel 

sobel_combine = cv2.bitwise_or(sobel_x,sobel_y)

titels = ['images','laplacian','sobel_x','sobel_y','sobel_combine']
images = [image,lap,sobel_x,sobel_y,sobel_combine] 

for i in range(5):
    plt.subplot(3,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titels[i])

plt.show()