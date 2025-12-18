import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable  # Add this import

def generate_launch_description():
    pkg_dir = get_package_share_directory('ball_pusher_robot')
    urdf_path = os.path.join(pkg_dir, 'urdf', 'ball_pusher.urdf')
    
    with open(urdf_path, 'r') as f:
        robot_desc = f.read()
    
    return LaunchDescription([
        # Force software rendering for VMware
        SetEnvironmentVariable('LIBGL_ALWAYS_SOFTWARE', '1'),
        
        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
        ),
        
        # Joint State Publisher GUI
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
        ),
        
        # RViz2 - Fixed version
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        ),
    ])
