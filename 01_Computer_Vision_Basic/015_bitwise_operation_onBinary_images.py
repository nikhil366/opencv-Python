'''
bitwise operation are very usefull when using it with mask. MASKS are very
usefull because it use in binary images and indicate where is any operation is 
perform.
'''
import cv2
import numpy as np

np_image = np.zeros((512,512,3), np.uint8)
rectangle_on_image = cv2.rectangle(np_image,(6,4),(223,502),(255,255,255), -1)

np_image01 = np.zeros((512,512,3), np.uint8)
rectangle_on_image01 = cv2.rectangle(np_image01,(300,10),(200,100),(255,255,255),-1)

'''bitwise AND operation (uncomment when run AND operation)'''
#bitAND = cv2.bitwise_and(np_image,np_image01)

'''bit OR operation'''


BitOR = cv2.bitwise_or(np_image,np_image01)


cv2.imshow('image_01',np_image01)
cv2.imshow('image', np_image)
#cv2.imshow('image_AND',bitAND)
cv2.imshow('image_OR',BitOR)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''as like OR and AND operator use XOR and NOT operator'''