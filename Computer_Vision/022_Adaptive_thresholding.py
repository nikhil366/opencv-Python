'''
Here in this segment we will understand about adaptive thresholding 
and also understand when we have simple image thresholding then why we need 
adaptive thresholding.

adaptive thresholding - 2 methods
1.  cv22.ADAPTIVE_THRESH_MEAN_C
2.  cv22.ADAPTIVE_THRESH_GAUSSIAN_C

'''


import cv2
import numpy as np

image_path = ('/home/nikhil/Desktop/Data/sudoku.png')
image = cv2.imread(image_path)

while True:
    ret, ATH = cv2.threshold(image,128,255,cv2.THRESH_BINARY)
    ad_thre = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    ''' 
    here we apply simple thresholding but cons is half image is not showing
    or it is cover with black colour so in this type of cases we cant use 
    simple thresholding.
    '''
    cv2.imshow('adptive_thresholding', ad_thre)
    cv2.imshow('simpleTH1',ATH)
    cv2.imshow('nrml_imag',image)

    k = cv2.waitKey(0)
    if k == 27 & 0xFF:
        break

cv2.destroyAllWindows()

