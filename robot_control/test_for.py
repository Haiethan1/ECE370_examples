from robot_control_class import RobotControl

rc = RobotControl()
test = rc.get_laser_full()

#exercise 3.3
maxVal = 0
for val in test:
    if val > maxVal:
        maxVal=val

print("farthest distance from wall is = ", maxVal)