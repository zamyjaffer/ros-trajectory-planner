# ROS Trajectory Planner

## Description
- This is a ROS project that creates a trajectory planner for an end-effector for a robots movement. This trajectory planner consists of 4 nodes:
  - 'points_generator' which generates random pramaters for the cubic trajectory.
  - 'compute_cubic_coeffs' which recieves the parameters from the first node and calculates foefficients for the trajectory.
  - 'cubic_traj_planner' which subscribes to the coefficients from the second node and generates the trajectory
  - 'plot_cubic_traj' which subsribes to the trajectory and plots the acceleration, position and velocity trajectories
- This project also consists of a launch file that starts the nodes and plots the trajectories as well as the graph of this project using rqt_plot and rqt_graph.

## Installation
- Download the 'ros_trajectory_planner' package into your catkin workspace 
- From the catkin workspace run the following command:
```
catkin_make
```

## Running
- from your catkin_workspace activate roscore: 
```
roscore
```

- from your catkin_workspace navigate to the scripts folder: 
```
cd /src/ros_trajectory_planner/scripts
```
    
- run the following commands from within the srcipts folder for each node:
```
chmod +x points_generator.py
chmod +x compute_cubic_coeffs.py
chmod +x cubic_traj_planner.py
chmod +x plot_cubic_traj.py
```
    
- navigate back to the catkin_ws folder: 
```
cd ~/ catkin_ws
```

- launch the package:
```
roslaunch ros_trajectory_planner cubic_traj_gen.launch
```

## Dependencies
- python 3.8.10
- ros-noetic
- numpy
