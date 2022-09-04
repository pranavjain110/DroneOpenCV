from djitellopy import Tello
import time

drone = Tello()

drone.connect()
print("Battery percentage:" ,drone.get_battery(), "\t Temperature: ",round((drone.get_temperature()-32)*5/9.0,2),"C")

drone.takeoff()

# drone.send_rc_control(left_right_velocity=40, forward_backward_velocity=0, up_down_velocity=0, yaw_velocity=45)
# time.sleep(2)

# drone.send_rc_control(left_right_velocity=-40, forward_backward_velocity=0, up_down_velocity=0, yaw_velocity=45)
# time.sleep(2)

# drone.send_rc_control(left_right_velocity=0, forward_backward_velocity=0, up_down_velocity=0, yaw_velocity=45)
# time.sleep(2)

drone.land()