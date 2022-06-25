#!/usr/bin/env python
# license removed for brevity
import rospy
import rospkg
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

class pathNode():


    def odom_callback(self,data):
        self.path.header = data.header
        pose = PoseStamped()
        pose.header = data.header
        pose.pose = data.pose.pose
        if not self.path.poses:
            self.path.poses.append(pose)
        elif abs(pose.pose.position.x - self.path.poses[-1].pose.position.x) < 0.5 and abs(pose.pose.position.y - self.path.poses[-1].pose.position.y) < 0.5:
            self.path.poses.append(pose)
        else:
            self.path.poses.clear()
            self.path.poses.append(pose)
        self.path_pub.publish(self.path)


    def __init__(self):

        rospy.init_node('path_node', anonymous=True)

        self.path = Path()

        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)

        self.path_pub = rospy.Publisher('/path', Path, queue_size=10)

        rospy.spin()



if __name__ == '__main__':
    try:
        pathNode = pathNode()
    except rospy.ROSInterruptException:
        pass