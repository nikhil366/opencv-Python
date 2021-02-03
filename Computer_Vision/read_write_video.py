import cv2

'''for use webcam we use function of number line 9 if you  wat to choose any video
from existing directory then we can use code of line 6 & 7'''

# video_path = "/home/Downloads/wetransfer-13f2a1/Video/test.mp4"
# video_captureture = cv2.Videovideo_captureture(video_path)

video_capture = cv2.VideoCapture(0)
'''if you want to use another USB camera then change VideoCapture(0) to VideoCapture(1 or 2 ) '''
fourcc = cv2.VideoWriter_fourcc(*'XVID')
'''fourcc is a video file which is use to generate a video like avi, mp4 etc.'''
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(video_capture.isOpened())
while(video_capture.isOpened()):
    ret, frame = video_capture.read()
    if ret == True:
       print(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
       print(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

       out.write(frame)

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == 27:
         break
    else:
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()