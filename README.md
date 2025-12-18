# PDE 4430 Mobile Robotics Coursework – ROS 2 Jazzy & Gazebo Harmonic

## INTRODUCTION

The objective is to design, model, and simulate a mobile robot using **ROS 2 Jazzy** and **Gazebo Harmonic**, and to demonstrate robot spawning, joint control, and basic teleoperation.

At the current stage, the robot has been successfully:

- Modelled using **URDF/XACRO**
- Built and organised as a **ROS 2 workspace**
- Spawned into **Gazebo Harmonic**
- Visualised and tested using **RViz**

  The package "ball_pusher_robot" contains the robot description and visualisation configuration.
  The package "my_bot_control" contains control and launch configurations for operating the robot in simulation.
  The package "assessment_world" contains the Gazebo simulation environment provided for the coursework assessment.

---

## Robot Description

The robot is a **four-wheeled mobile base** with additional **manipulation components**.

### Key Features
- Rectangular base link acting as the main body
- Four wheels:
  - Front-left
  - Front-right
  - Rear-left
  - Rear-right
- Continuous wheel joints
- Two arms:
  - Left arm
  - Right arm
- Each arm includes prismatic gripper finger

---

### RViz Visualisation

The robot was successfully visualised in RViz, 
" ros2 run robot_state_publisher robot_state_publisher ~/ros2/src/ball_pusher_robot/urdf/ball_pusher.urdf"
"ros2 run rviz2 rviz2"

confirming:

- Correct link hierarchy  
- Proper joint connections   
- Valid robot description 

---

## Gazebo Simulation

### Assessment world launch

The assessment world provided was succesfully launched inside the gazebo and balls and obstacles were also correct.
"ros2 launch assessment_world assessment_complete.launch.py"


### Spawning the Robot in Gazebo Harmonic

The robot was spawned into Gazebo Harmonic using a custom launch configuration.
"ros2 launch ball_pusher_robot spawn_robot.launch.py"

At this stage:

- The robot successfully appears in the Gazebo world  
- All major links and joints are visible  
- The model loads without errors    
- The robot interacts correctly with the Gazebo environment  
- Collisions with walls are detected
- The collision with balls were not perfect.

---

## Current Status

At the current stage of development, the project demonstrates:

- A complete robot model  
- Successful visualisation in RViz  
- Reliable spawning in Gazebo Harmonic  
- Basic movement with gazebo controller and environment interaction  

---

## Conclusion

This coursework successfully demonstrates the design, modelling, and simulation of a mobile robot using ROS 2 Jazzy and Gazebo Harmonic. The current implementation validates the robot model, simulation setup, and basic control pipeline, providing a solid foundation for further development and experimentation.

## References

- ChatGPT, Deepseek and Gemini (for error correction and gazebo issues)
- https://docs.ros.org/en/jazzy/Tutorials/URDF/URDF-Main.html
- https://docs.ros.org/en/jazzy/Tutorials/Using-RViz.html
- https://docs.ros.org/en/jazzy/p/robot_state_publisher/
- Google web browser 

The video presentation :- 
