''' In this we can understand how we can find out diffrent kind of functionality
of any thing in opencv-python
here in this file you will understand diffrent type of mouse event 
to check all the operations via mouse then check what kind of operation can 
perform with the help of mouse.'''

import cv2
import numpy

'''here we can check how many types of mouse event is present in cv2'''
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events) 

'''here you will get list of all Mouse Event'''
lst_of_mouse_operation = []

for i in dir(cv2):
    if 'EVENT' in i:
        lst_of_mouse_operation.append(i)
print(lst_of_mouse_operation)        


'''so in CV2 there are several number of mouse operations you can check the list

['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 
'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN',
 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 
 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 
 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
 
 '''

