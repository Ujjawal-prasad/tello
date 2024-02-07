import cv2
import numpy as np
from djitellopy import tello
import time

up = tello.Tello()
up.connect()
up.streamon()
up.takeoff()


w,h = 360,240
fbrange = [6200,6800]
pid = [0.4,0.4,0]
pError = 0


def face_detection(img):
    face_cascade = cv2.CascadeClassifier("Resorces/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imgGray,1.2,8)

    myfacelist = []
    myarealist = []

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)
        myfacelist.append([cx,cy])
        myarealist.append(area)
        if len(myarealist)!=0:
            i = myarealist.index(max(myarealist))
            return img, [myfacelist[i],myarealist[i]]
        else :
            return img, [[0,0],0]

def track_face(info,w,pid,pError):
    area = info[1]
    x,y = info[0]
    error = x - w//2
    fb = 0
    speed = pid[0]*error + pid[1]*(error-pError)
    speed = int(np.clip(speed,-100,100))
    
    if area ==0:fb=0
    elif area<fbrange[1] and area>fbrange[0]:fb = 0
    elif area<fbrange[0] and area != 0:fb = 20
    elif area>fbrange[1]:fb = -20

    if x == 0:
        speed = 0
        error = 0

    print(speed,fb)

    

    

    return error





while True:
    img = up.get_frame_read().frame
    img = cv2.resize(img,(w,h))
    result = face_detection(img)
    if result is not None:
        img, info = result
        #print("Center",info[0],"Area", info[1])
    else:
        info = [[0,0],0]
        #print("Center",info[0],"Area", info[1])
    pError=track_face(info,w,pid,pError)
    

    cv2.imshow("output",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        up.land()
        break