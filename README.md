# Robot Control Utils

This repository contains multiple utility programs and scripts developed during my MSc Thesis.

## Requirements
### Simulated mode
- Flatland Simulator (https://github.com/avidbots/flatland)
### Real Robot mode
- SERP (serp package in https://github.com/jorgef1299/SERP)
- rosserial (https://github.com/ros-drivers/rosserial)

## Installation

### Simulated mode
Within your catkin workspace, assuming the ROS environment is set up:
```
$ cd src/
$ git clone https://github.com/avidbots/flatland.git
$ git clone https://github.com/BerserkingIdiot/robot_control_utils_ros1.git
$ cd ..
$ rosdep install --from-paths src -i -y -r
$ catkin_make
```

### Real Robot mode
Within your catkin workspace, assuming the ROS environment is set up:
```
$ cd src/
$ git clone https://github.com/jorgef1299/SERP.git
$ git clone https://github.com/ros-drivers/rosserial.git
$ git clone https://github.com/BerserkingIdiot/robot_control_utils_ros1.git
$ cd ..
$ rosdep install --from-paths src -i -y -r
$ catkin_make
```

## How to run

### Simulated mode
- To launch environment with obstacles and rqt_robot_steering: `roslaunch robot_control_utils_ros1 flatland_obstacles.launch`
- To start saving data to CSV file: `rosrun robot_control_utils_ros1 csv_exporter.py \_output_file_path:=<FILE_NAME>.csv`
- To show data from a CSV file: `python plotter.py`
- To launch keyboard control of a robot: `rosrun robot_control_utils_ros1 teleop_keyboard`
- To publish trajectory data of a robot: `rosrun robot_control_utils_ros1 path_node.py`

### Real Robot mode
- To launch differential drive controller: `roslaunch robot_control_utils_ros1 diff_drive.launch`
- To launch differential drive controller for use with RL agent: `roslaunch robot_control_utils_ros1 diff_drive_rl_agent.launch`
