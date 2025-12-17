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
