#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from dofbot_interfaces.msg import Telemetry

class ArmCtrlNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__arm_state_pub = self.create_publisher(String, 'robot_name', 10)
        self.__arm_telemetry_pub = self.create_publisher(Telemetry, 'telemetry', 10)
        self.__arm_state_timer = self.create_timer(1.0, self.__on_armctrl_timer)
        self.__arm_telem_timer = self.create_timer(2.0, self.__on_armtel_timer)
        # self.__arm_ctrl_sub = self.create_subscription()
        self.get_logger().info(f"{node_name} inicializado...")

    def __on_armctrl_timer(self):
        mensaje = String()
        mensaje.data = "Dofbot X"
        self.__arm_state_pub.publish(mensaje)

    def __on_armtel_timer(self):
        telem_msg = Telemetry()
        telem_msg.activo = False
        telem_msg.robot_name = "DofbotX"
        telem_msg.ipaddr = "255.255.255.255"
        telem_msg.arm_joint_name = ['arm_joint1', 'arm_joint2', 'arm_joint3', 'arm_joint4', 'arm_joint5', 'gripper_joint']
        telem_msg.arm_joints = [0.0,0.0,0.0,0.0,0.0, -1.54]
        telem_msg.gripper_joint = 0.0
        telem_msg.arm_pose.position.x = 0.0
        telem_msg.arm_pose.position.y = 0.0
        telem_msg.arm_pose.position.z = 0.0
        telem_msg.arm_pose.orientation.w = 1.0
        telem_msg.arm_pose.orientation.x = 0.0
        telem_msg.arm_pose.orientation.y = 0.0
        telem_msg.arm_pose.orientation.z = 0.0
        self.__arm_telemetry_pub.publish(telem_msg)

def init_arm_ctrl(args=None):
    rclpy.init(args=args)
    armctrl_node = ArmCtrlNode('arm_ctrl')
    rclpy.spin(armctrl_node)
    rclpy.shutdown()

if __name__ == '__main__':
    init_arm_ctrl()
