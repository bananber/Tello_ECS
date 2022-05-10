from djitellopy import tello
from time import sleep

babner = tello.Tello()
babner.connect()
print(babner.get_battery())
