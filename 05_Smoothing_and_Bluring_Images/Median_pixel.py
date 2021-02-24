'''
Median pixel The Median blur operation is similar to the other averaging methods.
Here, the central element of the image is replaced by the median of all the pixels in
the kernel area. This operation processes the edges while removing the noise.
and it work more properly on black and white image.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.type_check import imag

image_path = ('/home/nikhil/Desktop/Data/cat.jpg')
image = cv2.imread(image_path, 0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5), np.float)/25

dst = cv2.filter2D(image, -1, kernal)
blur = cv2.blur(image,(5,5))
gaussian_blur = cv2.GaussianBlur(image,(5,5),0)
median_filter = cv2.medianBlur(image, 5)


titels = ['images','2D_Convolution', 'blur', 'gaussian_blur','median_filter']
images = [image, dst, blur, gaussian_blur, median_filter] 

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titels[i])

plt.show()