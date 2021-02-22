'''bilateral filter is used for image sharpening via this bilateral filter the 
edges or we can do sharpness of the images '''

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
Bilateral_filter = cv2.bilateralFilter(image, 9, 75 , 75 )


titels = ['images','2D_Convolution', 'blur', 'gaussian_blur','median_filter','bilateral_filter']
images = [image, dst, blur, gaussian_blur, median_filter, Bilateral_filter] 

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titels[i])

plt.show()