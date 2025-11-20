#!/usr/bin/env python3
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import rclpy
from rclpy.node import Node

class ConstantControlNode(Node):
    def __init__(self):
        super().__init__("constant_control")
        self.publisher_ = self.create_publisher(Twist, "/cmd_vel", 10)
        self.timer = self.create_timer(0.2, self.timer_callback)
        self.kill_sub = self.create_subscription(Bool,"/kill",self.kill_callback,10)

        self.killed = False
        self.get_logger().info("constant control node started")

    def timer_callback(self):
        if self.killed:
            return

        msg = Twist()
        msg.linear.x = 0.2 
        msg.angular.z = 0.0  
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing straight motion")

    def kill_callback(self, msg):
        if msg.data:
            self.killed = True
            stop_msg = Twist() 
            self.publisher_.publish(stop_msg)
            self.get_logger().info("Kill received: stopping robot")

def main(args=None):
    rclpy.init(args=args)
    node = ConstantControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


















