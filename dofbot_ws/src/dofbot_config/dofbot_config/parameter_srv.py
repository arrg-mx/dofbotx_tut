#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterDescriptor, SetParametersResult

class ParameterSrv(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        # 1. Para declara un solo parametro
        self.declare_parameter(
            'vel_default',
            0.01,
            descriptor=ParameterDescriptor(description="Velocidad por default del brazo")
        )
        # 1.1 Para leer el valor de un parametro
        self.__vel_arm = self.get_parameter('vel_default').get_parameter_value().double_value
        # 2. Para declarar multiples parametros
        self.declare_parameters(
            namespace='dofbot_config',
            parameters=[
                ('vel_lin', 0.25), # ROS utiliza metros como unidad lineal
                ('vel_ang', 0.15), # ROS utiliza radianes como unidad angular 
                ('joint_names', rclpy.Parameter.Type.STRING_ARRAY), # Definido como arreglo de tipo string
                ('gripper_joint_name', rclpy.Parameter.Type.STRING),
                ('robot_name', 'VIRTUAL'),
                ('robot_ip', rclpy.Parameter.Type.STRING)
            ]
        )
        self.__robot_name = self.get_parameter('dofbot_config.robot_name').get_parameter_value().string_value
        self.add_on_set_parameters_callback(self.__on_params_change)
        self.get_logger().info(f"Parameter Server [{node_name}] inicializado... Name: {self.__robot_name}, Vel arm (default) is {self.__vel_arm}")

    def __on_params_change(self, params:list[Parameter]):
        success = True
        # Para validar el valor(valores) deseado necesitamos recorrer
        # toda la lista de parametros
        for param in params:
            if param.name == 'vel_default':
                if param.value < 0.0 or param.value > 1.0:
                    self.get_logger().warn(f"Parameter {param.name} debe ser mayor a cero y menor a 1.0, valor a cambiar fue {param.value}")
                    success = False

            # TODO: Hacer ejemplos de validacion para otros parametros

        # Una vez obtenido el resultado
        # generar la respuesta (return) de la funcion
        result_msg = SetParametersResult()
        result_msg.successful = success
        result_msg.reason = "Proceso exitoso" if success else "Error en la valiacion"

        return result_msg                    

def init_param_srv(args=None):
    rclpy.init(args=args)
    param_srv_node = ParameterSrv('param_srv')
    rclpy.spin(param_srv_node)
    rclpy.shutdown()

if __name__ == "__main__":
    init_param_srv()