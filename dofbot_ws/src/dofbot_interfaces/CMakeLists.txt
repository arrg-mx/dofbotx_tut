cmake_minimum_required(VERSION 3.8)
project(dofbot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
# 1. Agregar las dependencias necesarias
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
# 1.1 Si se incluyen mensajes ya existentes propios (mios)
# o de ROS, se debe incluir la referencia al paquete que lo
# contiene
find_package(geometry_msgs REQUIRED)

# 2. Localizacion de los prototipos de mensaje
rosidl_generate_interfaces(${PROJECT_NAME}
  # Aqui agregamos las direcciones donde se encuentran 
  # los prototipos de mensaje
  "msg/Telemetry.msg"
  # "srv/MensajeServicio.srv"
  # "action/MensajeAccion.action"
  # 2.1. Dependencias necesarias para generar el mensaje declarado 
  # en su prototipo (Solo incluir si existe alguna)
  DEPENDENCIES geometry_msgs
)

# 3. Exportar el resultado de rosidl_generate_interfaces
# a la solucion en ROS2
ament_export_dependencies(rosidl_default_runtime)

ament_package()
