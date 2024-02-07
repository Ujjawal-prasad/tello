from djitellopy import tello
import audio_recognition as ar
import time 

up = tello.Tello()

up.connect()
print(up.get_battery())
up.takeoff()

while True:
    command = ar.communicate_to_drone()
    up.send_rc_control(0,0,0,0)
   
    if 'rotate' in command:
        while True:
            up.send_rc_control(0,0,0,25)
            ar.communicate_to_drone()
            if 'exit' in command:
                break
            time.sleep(0.1)
    
    elif 'land' in command:
        up.land()
        break

    time.sleep(0.1)


    

