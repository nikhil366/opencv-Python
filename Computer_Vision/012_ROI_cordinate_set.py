import cv2
import numpy as np

image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"

image = cv2.imread(image_path, 1)

face = image[50:250, 150:550]
print(face.shape)

cv2.imshow('image',face)
cv2.waitKey(0)
cv2.destroyAllWindows()