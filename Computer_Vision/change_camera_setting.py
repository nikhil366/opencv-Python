import cv2
import numpy as np

video_capture =  cv2.VideoCapture(0)
'''for check the value of width and height of screen/camera/image'''

print(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

'''for set a video frame height and width'''

video_capture.set(3,1270)
video_capture.set(4,3000)

print(video_capture.get(3))
print(video_capture.get(4))

while(video_capture.isOpened()):

    frame_value, frame = video_capture.read()

    if frame_value == True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video_capture.release()
cv2.destroyAllWindows()    


