import time
import cv2

video=cv2.VideoCapture(0)
face_cap=cv2.CascadeClassifier("C:/Users/PC/Desktop/python programs/facial_recognotion/.venv/Lib/site-packages/cv2/data/haarcascade_frontalcatface")
time.sleep(1)
while True:
    check,frame=video.read()
    key=cv2.waitKey(1)

    bnwframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",bnwframe)

    if key==ord("q"):
        break

