from os import sched_get_priority_max
import cv2
import dlib
import numpy as np

video_capture = cv2.VideoCapture(0)

'''here in this we are working on dlib lib of python to detect the face 
on webcam or we can detect face on any video'''

detector = dlib.get_frontal_face_detector()
dlib_face_det_path = ("/home/nikhil/Desktop/GazeTrack/shape_predictor_68_face_landmarks.dat")
predictor = dlib.shape_predictor(dlib_face_det_path)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   

    faces = detector(gray)
    for face in faces:
        # print(face)
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(gray, (x,y), (x1,y1), (0,255, 255), 3)
        cv2.rectangle(frame, (x,y), (x1,y1), (0,255, 255), 3)
    cv2.imshow('Gray_video',gray)
    cv2.imshow('video', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break