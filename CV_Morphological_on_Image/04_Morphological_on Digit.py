'''Morpholgical image operation have diffrent types but mainly we
can see the most use in images are as follow
1.dilation
2.erosion
3.opening(opening perform 1st erosion and then dilation)
4.closing(closing perform 1st dilation and erosion)
5.MORPH_GRADIENT
6.MORPH_TOPHAT
'''
import cv2 
import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.shape_base import get_array_prepare

image_path = ("/home/nikhil/Desktop/Data/j.png")
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

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image','mask','dilation','erosion', 'opening','closing', 'mg', 'th']
images = [img2,mask,dilation,erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.tight_layout()      
plt.show()  

