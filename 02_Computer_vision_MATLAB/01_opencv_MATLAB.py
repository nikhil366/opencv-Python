'''
Matplotlib is a comprehensive library for creating static
animated, and interactive visualizations in Python.
Matplotlib makes easy things easy and hard things possible

in this file we learn how we can open image via matplotlib
'''
import cv2
from matplotlib import pyplot as plt

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
image = cv2.imread(image_path)

while True:

    cv2.imshow('_nrml_image',image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image)
    plt.show()

    k = cv2.waitKey(0)
    if k == 27:
        break
    
cv2.destroyAllWindows()


