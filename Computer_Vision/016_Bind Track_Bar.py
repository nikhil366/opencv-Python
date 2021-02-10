'''Track Bar is use to change value dynamically or change value 
on runtime  of BGR we need track bar'''
import numpy  as np
import cv2 as cv

def nothing(x):
    print(x)

np_image = np.zeros((512,512,3), np.uint8)

cv.namedWindow('image') 

cv.createTrackbar('B','image',0, 255, nothing)   # it will change B channel value
cv.createTrackbar('G','image',0, 255, nothing)   # it will change G channel value
cv.createTrackbar('R','image',0, 255, nothing)   # it will change R channel value

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)


while(1):
    cv.imshow('image', np_image)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch, 'image')
    

    if s == 0:
       np_image[:] = 0
    else:
       np_image[:] = [b, g, r]

cv.destroyAllWindows()

