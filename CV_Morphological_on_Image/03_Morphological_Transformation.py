'''Morpholgical transform are some simple operation based on image shape
it is only perfromed on binary image'''

import cv2 
import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.shape_base import get_array_prepare

image_path = ("/home/nikhil/Desktop/Data/colorball.jpg")
img1 = cv2.imread(image_path,0)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

ret, mask = cv2.threshold(img2, 220, 255, cv2.THRESH_BINARY)
print(ret)

kernal = np.ones((5,5),np.uint8)
'''dilation is use to remove extra dots or noise from image'''
dilation = cv2.dilate(mask, kernal, iterations=2) # kernal is normaly a shape which we apply on image

'''erosion will help to  bring image shape or ball shape in 
acctual shape remove noise or spots from the image'''

erosion = cv2.erode(mask,kernal,iterations=1) 

'''
In morphological there is a new method we can use which combine both
erosion and dilation 
'''
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

titles = ['image','mask','dilation','erosion', 'opening']
images = [img2,mask,dilation,erosion, opening]

for i in range(5):
    plt.subplot(3,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.tight_layout()      
plt.show()  


'''Now understand morphological in a better way into next file
on morphological transform on word \J'''



