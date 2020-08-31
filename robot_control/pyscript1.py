from robot_control_class import RobotControl
# import Robot_control_class
import time as t

rc = RobotControl()
# rc2 = robot_control_class.RobotControl()

a = rc.get_laser(360)

print ("The distance measured is: ", a)

i = 225
while True:
    d = rc.get_laser_full()
    for i in range(0,719):
        dd = d[i]
        print("i = ", i, "d = ", dd)
        t.sleep(.1)
    print("i = ", i, "d = ", d)
    print(type(d))
    i = i + 1
    if( i > 719 ):
        i=0
    