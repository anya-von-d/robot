#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool


class ConstantControlNode(Node):
    def __init__(self):
        super().__init__("constant_control")
        self.publisher_ = self.create_publisher(Twist, "/cmd_vel", 10)
        self.timer_period = 0.2
        self.timer = self.create_timer(self.timer_period, self.timer_callback)

        self.kill_sub = self.create_subscription(Bool,"/kill",self.kill_callback,10,)
        self.get_logger().info("Constant control node started.")

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.5
        self.publisher_.publish(msg)
        log_text = ("Publishing cmd_vel: linear.x="+ str(msg.linear.x)+ ", angular.z="+ str(msg.angular.z))
        self.get_logger().info(log_text)

    def kill_callback(self, msg: Bool):
        if msg.data:
            self.get_logger().info("Kill signal received! Stopping robot.")

            if self.timer is not None:
                self.timer.cancel()

            stop_msg = Twist()
            stop_msg.linear.x = 0.0
            stop_msg.angular.z = 0.0
            self.publisher_.publish(stop_msg)
            self.get_logger().info("Robot stopped.")


def main(args=None):
    rclpy.init(args=args)
    node = ConstantControlNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

