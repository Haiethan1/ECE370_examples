from robot_control_class import RobotControl
import time as t

rc = RobotControl()

rc.stop_robot()

while True:
    d = rc.get_laser(360)
    if (d < 1.0):
        rc.stop_robot()
    else:
        rc.move_straight()
    print("d = ", d)