# Prototipo de mensaje de Telemetria
# ROS por default RADIANES para la posicion angular

bool activo false
string robot_name
string<=15 ipaddr    # 255.255.255.255
float64[5] arm_joints # Numero de articulaciones del brazo (5)
string[5] arm_joint_name # Nombre de las articulaciones
float32 gripper_joint # Posicion de la pinza
# Posicion en X, Y, Z, Orientacion en  pitch, roll, yaw ???
geometry_msgs/Pose arm_pose
