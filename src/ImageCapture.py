from djitellopy import Tello
import time
import cv2
drone = Tello()

drone.connect()
print("Battery percentage:" ,drone.get_battery(), "\t Temperature: ",round((drone.get_temperature()-32)*5/9.0,2),"C")

drone.stream_on()

while True:

    img = drone.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    #display image in a window and keep it open for 1ms
    cv2.imshow("Drone Image",img)  
    cv2.wait(1) #1ms