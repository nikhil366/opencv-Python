'''Here in this we will discuss about gaussian filter
 gaussian filter - is use to remove high frequency noise from image'''
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

titels = ['images','2D_Convolution', 'blur', 'gaussian_blur']
images = [image, dst, blur, gaussian_blur] 

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titels[i])

plt.show()