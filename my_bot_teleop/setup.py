from setuptools import setup
import os
from glob import glob

package_name = 'my_bot_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # If you have launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # If you have config files
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='Teleoperation package for my robot',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['teleop_node = my_bot_teleop.teleop_node:main','keyboard_teleop = my_bot_teleop.keyboard_teleop:main',
            # Add your executable scripts here
            # 'teleop_node = my_bot_teleop.teleop_node:main',
        ],
    },
)
