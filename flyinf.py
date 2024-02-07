from djitellopy import tello
from time import sleep
tello1 = tello.Tello()
tello1.connect()

print(tello1.get_battery())

