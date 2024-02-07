from djitellopy import tello
import key_press as kp
import time
import cv2

kp.init()

up = tello.Tello()
up.connect()
print(up.get_battery())
up.streamon()



def keyboard_inputs():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getkey("q"): up.takeoff()
    elif kp.getkey("e"): up.land()
    elif kp.getkey("UP"): fb = speed
    elif kp.getkey("DOWN"):fb = -speed
    elif kp.getkey("LEFT"):lr = -speed
    elif kp.getkey("RIGHT"):lr = speed
    elif kp.getkey("a"): yv = -speed
    elif kp.getkey("d"): yv = speed
    elif kp.getkey("w"): ud = speed
    elif kp.getkey("s"): ud = -speed
    elif kp.getkey("z"):
        cv2.imwrite(f'tello/survalliance_images/{time.time()}.jpg',img)
        time.sleep(0.3)
        
    return[lr, fb, ud, yv]

while True:
    vals = keyboard_inputs()
    up.send_rc_control(vals[0],vals[1],vals[2],vals[3])
    time.sleep(0.01)
    img = up.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("eyes of tello",img)
    cv2.waitKey(1)
    