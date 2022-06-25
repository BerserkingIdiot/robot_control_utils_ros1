#include "ros/ros.h"
#include <serp/Velocity.h>
#include <serp/RobotInfo.h>
#include <geometry_msgs/Twist.h>
#include <cmath>

//in meters
#define WHEEL_SPACING 0.145
#define WHEEL_RADIUS 0.035 

serp::RobotInfo robotget;
ros::Publisher send_velocities;

/*
bool printRobotInfo(std_srvs::TriggerRequest &req, std_srvs::TriggerResponse &res) 
{
    res.success = true;
    res.message = std::to_string(robotget.battery_level);
    return true;
}

void getInfo(const serp::RobotInfo &msg)
{
    robotget.battery_level=msg.battery_level;
    robotget.vel_linear=msg.vel_linear;
    robotget.vel_angular=msg.vel_angular;
}
*/

void processTwist(const geometry_msgs::Twist &vel_twist_msg) 
{
    double lin_vel, ang_vel = 0;

    lin_vel = vel_twist_msg.linear.x;
    ang_vel = vel_twist_msg.angular.z;

    if(std::isnan(lin_vel) || std::isnan(ang_vel)){return;}

    ROS_INFO_STREAM( "Received velocity command:"
    << " linear=" << lin_vel
    << " angular=" << ang_vel);

    serp::Velocity vel_cmd;

    double left = (lin_vel - ang_vel * WHEEL_SPACING / 2.0) / WHEEL_RADIUS;
    double right = (lin_vel + ang_vel * WHEEL_SPACING / 2.0) / WHEEL_RADIUS;

    
    if(left<-90){left=-90;}
    else if(left>90){left=90;};
    if(right<-90){right=-90;}
    else if(right>90){right=90;};
    

    ROS_INFO_STREAM( "Sending velocity command:"
    << " left=" << left
    << " right=" << right);

    vel_cmd.vel_motor_left = left;
    vel_cmd.vel_motor_right = right;

    send_velocities.publish(vel_cmd);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "differential_drive_controller");
    ros::NodeHandle nh;
    serp::Velocity vel_cmd;

    //ros::ServiceServer service_battery = nh.advertiseService("print_robot_info", printRobotInfo);

    send_velocities = nh.advertise<serp::Velocity>("motors_vel", 2);
    //ros::Subscriber receive_info = nh.subscribe("hardware_info", 2, getInfo);
    ros::Subscriber receive_twist = nh.subscribe("cmd_vel", 1000, processTwist);

    ros::spin();
}