import cv2

# Load video from our System

video_path = "/home/Downloads/wetransfer-13f2a1/Video/test.mp4"
video_capture = cv2.Videovideo_captureture(video_path)

while(video_capture.isOpened()):
    ret, frame = video_capture.read()
    '''here ret will store the boolean value 
    if camera is open then ret == True otherwise False
    and Frame will store the frames of videos or we can say 
    it will convert video into images'''
    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
         break
    else:
        break

video_capture.release()
cv2.destroyAllWindows()