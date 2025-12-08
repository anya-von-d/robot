#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped


class Navigator(Node):
    def __init__(self):
        super().__init__('navigator')

        # subscribe to the goal pose that rviz_goal_relay publishes
        self.goal_sub = self.create_subscription(
            PoseStamped,
            '/cmd_nav',
            self.goal_callback,
            10
        )

        self.get_logger().info('Navigator node started, waiting for /cmd_nav goals...')

    def goal_callback(self, msg: PoseStamped) -> None:
        self.get_logger().info(
            f"Received goal: x={msg.pose.position.x:.2f}, "
            f"y={msg.pose.position.y:.2f}, "
            f"theta (quat z)={msg.pose.orientation.z:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = Navigator()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

   



