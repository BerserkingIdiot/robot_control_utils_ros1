# Tairema_ROS1

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
$ git clone https://github.com/BerserkingIdiot/Tairema_ROS1.git
$ cd ..
$ rosdep install --from-paths src -i -y -r
$ catkin_make
```
## How to run
### Simulated mode
- To launch environment with obstacles and rqt_robot_steering: roslaunch tairema_ros1 flatland_obstacles.launch
- To start saving data to CSV file: rosrun tairema_ros1 csv_exporter.py \_output_file_path:=<FILE_NAME>.csv
