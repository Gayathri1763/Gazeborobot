# PDE 4430 Mobile Robotics Coursework – ROS 2 Jazzy & Gazebo Harmonic

## INTRODUCTION

The objective is to design, model, and simulate a mobile robot using **ROS 2 Jazzy** and **Gazebo Harmonic**, and to demonstrate robot spawning, joint control, and basic teleoperation.

At the current stage, the robot has been successfully:

- Modelled using **URDF/XACRO**
- Built and organised as a **ROS 2 workspace**
- Spawned into **Gazebo Harmonic**
- Visualised and tested using **RViz**

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
- Each arm includes:
  - One revolute joint
  - Two prismatic gripper fingers

---

### RViz Visualisation

The robot was successfully visualised in RViz, confirming:

- Correct link hierarchy  
- Proper joint connections   
- Valid robot description 

---

## Gazebo Simulation

### Assessment world launch

The assessmnet world provided was succesfully launched inside the gazebo and balls and obstacles were also correct.


### Spawning the Robot in Gazebo Harmonic

The robot was spawned into Gazebo Harmonic using a custom launch configuration.

At this stage:

- The robot successfully appears in the Gazebo world  
- All major links and joints are visible  
- The model loads without errors    
- The robot interacts correctly with the Gazebo environment  
- Collisions with walls are detected
- The collision with balls where not perfect.

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

The video presentation :- 
