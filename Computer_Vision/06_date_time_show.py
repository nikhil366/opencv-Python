'''here in this you will understand how you can put some text or date and time on 
running webcam or video'''
import cv2
import datetime

video_capture =  cv2.VideoCapture(0)

print(video_capture.get(3))
print(video_capture.get(4))

#


while (video_capture.isOpened()):
    frame_value, frame = video_capture.read()

    if frame_value == True:

        font = cv2.FONT_HERSHEY_PLAIN
        date_time = str(datetime.datetime.now())
        text = 'width :' + str(video_capture.get(3)) + 'Height :' +  str(video_capture.get(4))
        frame = cv2.putText(frame, text, (5,50), font, 3, (255,0,255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, date_time, (13,350), font, 3, (255,0,0), 2, cv2.LINE_AA)
        cv2.imshow('video', frame)

        k =  cv2.waitKey(1)

        if k == 27:
            break


    else:
        break
  

video_capture.release()
cv2.destroyAllWindows()