import cv2
import numpy as np

'''here this code is use for choose image from our systemand show in new window'''
image_path = "/home/nikhil/Pictures/Webcam/nik.jpg"
# img = cv2.imread(image_path, -1)
img = np.zeros([512,512,3],np.uint8)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

'''by default k == 27 is value of Esc of our keyboard'''

if k == 27:
  cv2.destroyAllWindows()
  '''ord is function  in which we can define and on press of this button video will save'''
elif k == ord('s'):    
  cv2.imwrite('image_copy', img)
  cv2.destroyAllWindows()