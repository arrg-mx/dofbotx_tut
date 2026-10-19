#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ArmCtrlNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__arm_state_pub = self.create_publisher(String, 'robot_name', 10)
        self.__arm_state_timer = self.create_timer(1.0, self.__on_armctrl_timer)
        # self.__arm_ctrl_sub = self.create_subscription()
        self.get_logger().info(f"{node_name} inicializado...")

    def __on_armctrl_timer(self):
        mensaje = String()
        mensaje.data = "Dofbot X"
        self.__arm_state_pub.publish(mensaje)

def init_arm_ctrl(args=None):
    rclpy.init(args=args)
    armctrl_node = ArmCtrlNode('arm_ctrl')
    rclpy.spin(armctrl_node)
    rclpy.shutdown()

if __name__ == '__main__':
    init_arm_ctrl()
