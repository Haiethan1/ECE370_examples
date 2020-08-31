from robot_control_class import RobotControl

rc = RobotControl()

#exercise 3.1 and 3.2
while(1):
    test = rc.get_laser(360)
    if(test < 1):
        rc.stop_robot()
        print("Too close, laser value = ", test)
    else:
        rc.move_straight()
        print("laser value = ", test)