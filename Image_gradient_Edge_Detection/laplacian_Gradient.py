'''Here in this we will discuss about laplasien derivative
laplacian function use to calculate the laplacian derivative
here in this we will discuss about laplacian gradient'''


import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.type_check import imag

image_path = ('/home/nikhil/Desktop/Data/ni.jpg')
image = cv2.imread(image_path, 0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(image, cv2.CV_64F, ksize=5)
# just a data type 64bit float and use for transforming image from white to black
# and it deals with negative number in our image
lap = np.uint8(np.abs(lap))

titels = ['images','laplacian']
images = [image,lap] 

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titels[i])

plt.show()