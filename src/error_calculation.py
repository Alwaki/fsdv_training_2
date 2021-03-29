#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
import math as m

class Listener:
    """Object which subscribes to topic and performs callback method"""
    def __init__(self):
        """Initialize node and create subscriber"""
        rospy.init_node("listener", anonymous=True)
        self.sub = rospy.Subscriber("/output", Odometry, 
                                    self.callback, queue_size=100)
        self.sub = rospy.Subscriber("/gnss", Odometry, 
                                    self.callback1, queue_size=100)
        self.x_recent = 0
        self.y_recent = 0
        self.error = 0
    
    def callback(self, data):
        """Stores position data in attributes"""
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y
        if x != self.x_recent:
            self.x_recent = x
        if y != self.y_recent:
            self.y_recent = y

    def callback1(self, data):
        """Calculates sum of error between fused data and GPS pose"""
        x1 = data.pose.pose.position.x
        y1 = data.pose.pose.position.y
        euclid_distance = m.hypot(self.x_recent-x1, self.y_recent-y1)
        self.error = self.error + euclid_distance
        rospy.loginfo("Sum of error is: " + str(self.error))
        
if __name__ == '__main__':
    try:
        sub = Listener()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass