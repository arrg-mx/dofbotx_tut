# Tutorial DOFBot

![ROS2 Jazzy](https://img.shields.io/badge/ROS2-Jazzy-blue.svg)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)

---

## Descripción

Este repositorio contiene un tutorial para controlar el brazo robótico DOFBot usando ROS 2 Jazzy. Proporciona un espacio de trabajo estructurado con paquetes, documentación y materiales de referencia para aprender desarrollo ROS 2 para manipulación robótica.

---

## Estructura del Repositorio

```
dofbotx_tut/
├── docs/                    # Documentación y referencias
│   └── refs/                # Materiales de referencia (hojas de datos, enlaces, especificaciones)
├── dofbot_ws/               # Espacio de trabajo ROS 2 Jazzy
│   └── src/
│       └── dofbot_ctrl/     # Paquete de control DOFBot (Python, ament_python)
└── README.md                # Este archivo
```

### Detalles de Carpetas

| Carpeta | Propósito |
|---------|-----------|
| `docs/` | Guías, tutoriales, documentación API |
| `docs/refs/` | Hojas de datos, enlaces externos, especificaciones de hardware |
| `dofbot_ws/src/dofbot_ctrl/` | Paquete ROS 2 para control del brazo |

---

## Inicio Rápido

### Requisitos Previos
- ROS 2 Jazzy instalado (ver [documentación oficial](https://docs.ros.org/en/jazzy/Installation.html))
- Python 3.10+
- Herramienta de compilación `colcon`

### Compilar y Ejecutar

```bash
# Clonar repositorio
git clone <url-del-repositorio>
cd dofbotx_tut/dofbot_ws

# Compilar espacio de trabajo
colcon build --symlink-install

# Cargar entorno
source install/setup.bash

# Ejecutar nodos (cuando estén implementados)
# ros2 run dofbot_ctrl <nombre_nodo>
```

---

## Paquete: dofbot_ctrl

| Propiedad | Valor |
|-----------|-------|
| **Nombre** | `dofbot_ctrl` |
| **Tipo** | Paquete Python (ament_python) |
| **Descripción** | Paquete de control del brazo DOFBot |
| **Versión** | 0.0.0 |
| **Mantenedor** | Felipe Rivas <rivascf@gmail.com> |
| **Licencia** | MIT |

### Estructura del Paquete

```
dofbot_ctrl/
├── dofbot_ctrl/          # Módulo Python
├── resource/             # Archivos de recursos
├── test/                 # Archivos de prueba
├── package.xml           # Manifiesto del paquete
├── setup.py              # Configuración paquete Python
├── setup.cfg             # Configuración setuptools
└── LICENSE               # Licencia MIT
```

---

## Desarrollo

### Pruebas

```bash
# Ejecutar todas las pruebas
colcon test

# Ver resultados de pruebas
colcon test-result --verbose
```

### Linting y Estilo

```bash
# Linting Python (flake8)
ament_flake8 dofbot_ws/src/dofbot_ctrl

# Estilo docstrings (pep257)
ament_pep257 dofbot_ws/src/dofbot_ctrl

# Encabezados de copyright
ament_copyright dofbot_ws/src/dofbot_ctrl
```

### Compilar Paquete Específico

```bash
colcon build --packages-select dofbot_ctrl --symlink-install
```

---

## Documentación

- **`docs/`** — Guías tutorial, documentación API, artículos cómo-hacer
- **`docs/refs/`** — Hojas de datos hardware, documentos especificación, enlaces referencia externos

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT — vea el archivo [LICENSE](LICENSE) para detalles.

---

## Mantenedor

**Felipe Rivas** — <rivascf@gmail.com>

---

## Enlaces Útiles

- [Documentación ROS 2 Jazzy](https://docs.ros.org/en/jazzy/)
- [Tutoriales ROS 2](https://docs.ros.org/en/jazzy/Tutorials.html)
- [Guía de usuario ament_python](https://docs.ros.org/en/jazzy/How-To-Guides/Ament-CMake-User-Guide.html)
- [Referencia hardware DOFBot](docs/refs/) *(agregue sus archivos de referencia aquí)*