import cv2
import streamlit as st
import time

date=time.strftime("%a")
current_time=time.strftime("%H:%M:%S %p")

st.title("Motion detector")
start = st.button("Start Camera")

if start :
    streamlit_image=st.image([])
    video = cv2.VideoCapture(0)

    while True:
        check ,frame = video.read()
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)

        cv2.putText(img=frame,text=date,org=(50,50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,0,0),
                    thickness=2,lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=current_time, org=(50, 100),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)
        streamlit_image.image(frame)

    video.release()

