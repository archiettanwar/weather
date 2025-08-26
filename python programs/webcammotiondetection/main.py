from emailing import send_email
import cv2
import time
import glob
import os
from threading import Thread

def clean_folder():
    images=glob.glob("images/*.png")
    for image in images:
        os.remove(image)

video=cv2.VideoCapture(0)
time.sleep(1)

first_frame=None
status_list=[]
count=0

while True:
    status=0
    check,frame=video.read()

    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame_blurred=cv2.GaussianBlur(gray_frame,(21,21),0)
    key=cv2.waitKey(1)

    if first_frame is None:
        first_frame=gray_frame_blurred

    del_frame=cv2.absdiff(first_frame,gray_frame_blurred)
    thresh_frame=cv2.threshold(del_frame,30,255,cv2.THRESH_BINARY)[1]
    dil_frame=cv2.dilate(thresh_frame,None,iterations=2)
    cv2.imshow("my video",dil_frame)

    contours,check=cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)<5000:
            continue
        x,y,w,h=cv2.boundingRect(contour)
        rectangle=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,225),3)
        if rectangle.any():
            status=1
            cv2.imwrite(f"images/{count}.png",frame)
            count=count+1
            all_images=glob.glob("images/*.png")
            index=int(len(all_images)/2)
            image_w_obj=all_images[index]


    status_list.append(status)
    status_list=status_list[-2:]
    print(status_list)

    if status_list[0]==1 and status_list[1]==0:
        sending_thread=Thread(target=send_email,args=(image_w_obj,))
        sending_thread.daemon=True
        clean_thread=Thread(target=clean_folder)
        clean_thread.daemon=True

        sending_thread.start()


    cv2.imshow("Video",frame)

    if key==ord("q"):
        break

video.release()
clean_thread.start()