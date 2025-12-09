from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get package directory
    pkg_dir = get_package_share_directory('ball_pusher_robot')
    
    # Read URDF file
    urdf_file = os.path.join(pkg_dir, 'urdf', 'ball_pusher.urdf')
    with open(urdf_file, 'r') as f:
        robot_desc = f.read()
    
    # Node to publish robot state from URDF
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )
    
    # Node to spawn robot in Gazebo
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', '/robot_description',
            '-name', 'ball_pusher',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.2'
        ],
        output='screen'
    )
    
    return LaunchDescription([
        robot_state_publisher,
        spawn_entity
    ])
