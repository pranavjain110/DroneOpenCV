import KeyPressModule as kp
from djitellopy import Tello
import time
import cv2

kp.init()
drone = Tello()

drone.connect()
print("Battery percentage:" ,drone.get_battery(), "\t Temperature: ",round((drone.get_temperature()-32)*5/9.0,2),"C")

drone.stream_on()
drone.takeoff()

global image

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

    # Capturing and saving image
    if kp.getKey("c"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg',img)
        #add time delay here of 300 ms if many pics are being clicked

    return [lr,fb,ud,yv]
while True:

    img = drone.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    #display image in a window and keep it open for 1ms
    cv2.imshow("Drone Image",img) 

    val = getKeyboardInput()
    drone.send_rc_control(val[0],val[1],val[2],val[3])  

    cv2.waitkey(1) #1ms