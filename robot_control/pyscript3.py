from robot_control_class import RobotControl
import time

rc = RobotControl()

#exercise 4.1
#def move_x_seconds(secs):
#    rc.move_straight()
#    time.sleep(secs)
#    rc.stop_robot()


#move_x_seconds(5)

#exercise 4.2
def get_laser_values( a, b, c):
    r1 = rc.get_laser_summit(a)
    r2 = rc.get_laser_summit(b)
    r3 = rc.get_laser_summit(c)
    
    return [r1, r2, r3]

test = get_laser_values(0, 500, 700)
print("reading 1: ", test[0])
print("reading 2: ", test[1])
print("reading 3: ", test[2])