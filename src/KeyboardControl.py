import KeyPressModule as kp
from djitellopy import Tello
import time

kp.init()
drone = Tello()

drone.connect()
print("Battery percentage:" ,drone.get_battery(), "\t Temperature: ",round((drone.get_temperature()-32)*5/9.0,2),"C")

drone.takeoff()

def getKeyboardInput():
    lr,fb,ud,yv = 0
    speed = 10

    # Setting vel for left-right motion
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    # Setting vel for forward-backward motion
    if kp.getKey("UP"): fb = -speed
    elif kp.getKey("DOWN"): fb = speed

    # Setting vel for up-down motion
    if kp.getKey("w"): ud = -speed
    elif kp.getKey("s"): ud = speed

    # Setting yaw vel
    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    # Takeoff and land
    if kp.getKey("t"): drone.takeoff()
    elif kp.getKey("l"): drone.land()

    return [lr,fb,ud,yv]
while True:

    val = getKeyboardInput()

    drone.send_rc_control(val[0],val[1],val[2],val[3])  
    time.sleep(0.1)