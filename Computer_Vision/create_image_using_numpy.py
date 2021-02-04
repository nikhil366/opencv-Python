import cv2
import numpy as np

'''create a blank image using numpy'''

numpy_image = np.zeros([512,512,3],np.uint8)

'''for draw a line on image'''
line_on_image = cv2.line(numpy_image,(0,0), (255,255), (255,0,0), 2)
'''for draw a arrow line on image'''
arrow_on_image = cv2.arrowedLine(numpy_image,(0,255),(255,255),(0,0,255), 4)

cv2.imshow("black_image", numpy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()