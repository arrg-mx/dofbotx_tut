from setuptools import find_packages, setup

package_name = 'dofbot_ctrl'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Felipe Rivas',
    maintainer_email='rivascf@gmail.com',
    description='Dofbot arm control package',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'armctrl = dofbot_ctrl.armctrl:init_arm_ctrl',
            'armctrl_sub = dofbot_ctrl.armctrlsub:init_armctrl_sub'
        ],
    },
)
