import cv2 
from matplotlib import pyplot as plt

def nothing(x):
    print(x)

image_path = ('/home/nikhil/Desktop/Data/ni.jpg')
image = cv2.imread(image_path, 0)
imagess = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

cv2.namedWindow('canny')

# add ON/OFF switch to "canny"
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'canny', 0, 1, nothing)

# add lower and upper threshold slidebars to "canny"
cv2.createTrackbar('lower', 'canny', 0, 255, nothing)
cv2.createTrackbar('upper', 'canny', 0, 255, nothing)

while True:
    # get current positions of four trackbars
    lower = cv2.getTrackbarPos('lower', 'canny')
    upper = cv2.getTrackbarPos('upper', 'canny')
    s = cv2.getTrackbarPos(switch, 'canny')
    if s == 0:
        edges = imagess
    else:
        edges = cv2.Canny(image, lower, upper)
    # display images
    cv2.imshow('original', imagess)
    cv2.imshow('canny', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   # hit escape to quit
        break

cv2.destroyAllWindows()

