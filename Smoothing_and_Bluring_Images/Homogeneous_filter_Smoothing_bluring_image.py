'''Here we will discuss about smoothing and bluring image basically its mean removing noise 
from the image
for blur image or smooth there are various filter 
1. homogeneous filter
2. Gaussian Filter
3 Median Filter
4. Bilateral Filter
'''
# Homogeneous filter (2D filter)
# via this filter we can remove noise or going to little bit blured.

import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.type_check import imag

image_path = ('/home/nikhil/Desktop/Data/Boxplot.png')
image = cv2.imread(image_path, 0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5), np.float)/25

dst = cv2.filter2D(image, -1, kernal)
blur = cv2.blur(image,(5,5))

titels = ['images','2D_Convolution', 'blur']
images = [image, dst, blur]

for i in range(3):
    plt.subplot(1,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titels[i])

plt.show()