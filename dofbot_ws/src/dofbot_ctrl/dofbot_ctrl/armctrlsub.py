#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ArmCtrlSub(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__armctrl_sub = self.create_subscription(String, '/robot_name', self.__on_msg_received, 10)
        self.get_logger().info(f"Node {node_name} inicializado...")

    def __on_msg_received(self, msg:String):
        self.get_logger().info(f"Recibi mensaje: {msg.data}")

def init_armctrl_sub(args=None):
    rclpy.init(args=args)
    armctrl_sub = ArmCtrlSub('armctrl_sub_node')
    rclpy.spin(armctrl_sub)
    rclpy.shutdown()

if __name__ == "__main__":
    init_armctrl_sub()