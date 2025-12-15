#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import tty
import termios

class KeyboardTeleop(Node):
    def __init__(self):
        super().__init__('keyboard_teleop')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('Keyboard Teleop Node Started')
        self.get_logger().info('Use WASD to control, Q to quit')
        
        self.linear_speed = 0.2
        self.angular_speed = 0.5
        
    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
    def run(self):
        try:
            while rclpy.ok():
                key = self.get_key()
                msg = Twist()
                
                if key == 'w':
                    msg.linear.x = self.linear_speed
                elif key == 's':
                    msg.linear.x = -self.linear_speed
                elif key == 'a':
                    msg.angular.z = self.angular_speed
                elif key == 'd':
                    msg.angular.z = -self.angular_speed
                elif key == 'q':
                    break
                else:
                    msg.linear.x = 0.0
                    msg.angular.z = 0.0
                
                self.publisher.publish(msg)
                self.get_logger().info(f'Published: linear={msg.linear.x}, angular={msg.angular.z}')
                
        except Exception as e:
            self.get_logger().error(f'Error: {e}')
        finally:
            msg = Twist()
            self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = KeyboardTeleop()
    node.run()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
