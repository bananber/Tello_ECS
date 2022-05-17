from djitellopy import tello
from time import sleep

babner = tello.Tello()
babner.connect()
print(babner.get_battery())
# must be facing leftside wall
# take off at 200cm
babner.takeoff()
babner.moveup(120)
# move forward 310cm
babner.move_forward(310)
sleep(1)
# turn
babner.rotate_clockwise(90)
sleep(1)
# move forward 800cm
babner.move_forward(500)
sleep(1)
babner.move_forward(300)
sleep(1)
# turn
babner.rotate_clockwise(90)
sleep(1)
# cool slip
babner.flip_forward()
sleep(1)
# move forward 310cm
babner.move_forward(310)
sleep(1)
# turn
babner.rotate_clockwise(90)
sleep(1)
# move forward 800cm
babner.move_forward(500)
sleep(1)
babner.move_forward(300)
sleep(1)
# landing
babner.land()
