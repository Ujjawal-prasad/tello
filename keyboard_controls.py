from djitellopy import tello
import key_press as kp
from time import sleep


kp.init()

up = tello.Tello()
up.connect()
print(up.get_battery())


def keyboard_inputs():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 100

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
    return[lr, fb, ud, yv]

while True:
    vals = keyboard_inputs()
    up.send_rc_control(vals[0],vals[1],vals[2],vals[3])
  
    
    sleep(0.01)
    
