from robot_control_class import RobotControl

rc = RobotControl()

#exercise 4.3
#rc.move_straight_time("forward", 1.0, 5)
#rc.turn("clockwise", 190, 7)

#exercise 4.4
rc.move_straight_time("forward", 1.0, 2)
rc.turn("clockwise", 1.0, 7)
rc.move_straight_time("forward", 1.0, 2.2)
rc.turn("clockwise", 1.0, 7)
rc.move_straight_time("forward", 1.0, 5)
