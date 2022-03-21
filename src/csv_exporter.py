#!/usr/bin/env python
# license removed for brevity
import rospy
import rospkg
from sensor_msgs.msg import LaserScan
import tf
import csv
import sys

import os

class csvExporterNode():


    def lidar_callback(self,data):

        #do things
        try:
            (trans,rot) = self.listener.lookupTransform('/map', '/base_link', rospy.Time(0))
            #print("trans is: ")
            #print(*trans, sep = ", ") 
            #print("rot is: ")
            #print(*rot, sep = ", ") 

            row = [ data.header.stamp.secs, data.header.stamp.nsecs, trans[0], trans[1], rot[2]] + list(data.ranges)

            self.writer.writerow(row)

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print("Missed a tf frame")

        #print("scan timestamp is: ", data.header.stamp.secs, " sec, ", data.header.stamp.nsecs, " nsec")
        #print("scan data is: ")
        #print(*data.ranges, sep = ", ")

        


    def __init__(self):

        rospy.init_node('csv_exporter', anonymous=True)

        print(os.getcwd())

        #sys.argv = rospy.myargv(argv=sys.argv)
        #if len(sys.argv) >= 2 :
        #    print("Too many arguments")
        #    return
        #elif len(sys.argv) == 2 :
        #    self.file_path = sys.argv[1]
        #else :
        #    self.file_path = "test.csv"
        
        self.file_path = rospy.get_param('~output_file_path','test.csv')

        self.output_file = open("src/tairema_ros1/output/" + self.file_path, "w")

        self.writer = csv.writer(self.output_file)

        header = ["timestamp secs", "timestamp nsecs", "x", "y", "rotation", "ranges"]
        self.writer.writerow(header)

        self.listener = tf.TransformListener()

        rospy.Subscriber(
                "/lidar_scan", 
                LaserScan,
                self.lidar_callback,
                buff_size=10000000,
                queue_size=1)

        rospy.spin()

        self.output_file.close()

        print("do we ever get here?")
        



if __name__ == '__main__':
    try:
        csvExpNode = csvExporterNode()
    except rospy.ROSInterruptException:
        pass