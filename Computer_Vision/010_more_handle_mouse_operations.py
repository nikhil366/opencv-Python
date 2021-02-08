import cv2 
import numpy as np


image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image = cv2.imread(image_path, 1)
print(image.shape)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = image[x, y, 0]
        green = image[x, y, 1]
        red = image[x, y, 2]

        cv2.circle(image, (x,y), 3, (0,0,255), -1)
        black_image = np.zeros((480,640,3), np.uint8)

        black_image[:] = [blue, green, red]

        cv2.imshow('image', black_image)

cv2.imshow('image', image)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()