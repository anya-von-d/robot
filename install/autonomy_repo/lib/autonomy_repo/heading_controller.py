#!/usr/bin/env python3
import numpy as np
import rclpy

from asl_tb3_lib.control import BaseHeadingController
from asl_tb3_lib.math_utils import wrap_angle
from asl_tb3_msgs.msg import TurtleBotState, TurtleBotControl

class HeadingController(BaseHeadingController):
    def __init__(self):
        super().__init__("heading_controller")
        self.declare_parameter("kp",2.0)
    def kp(self):
    	return float(self.get_parameter("kp").value)
    def compute_control_with_goal(self,TurtleBotState,TurtleBotState) :
        err = wrap_angle(goal.theta - state.theta)
        cmd = TurtleBotControl()
        cmd.omega = float(self.kp * err)
        return cmd
def main() :
    rclpy.init()
    node = HeadingController()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
if __name__ == "__main__":
    main()

