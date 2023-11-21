# in this we include both publisher and subsriber to create a closed loop

#! /usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


def pose_callback(pose):
    cmd = Twist()
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    # elif pose.y > 9.0:
    #     cmd.linear.y = 1.0
    #     cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    # cmd.linear.x = 5.0
    # cmd.angular.z = 0.0
    pub.publish(cmd)

if __name__ == '__main__':

    rospy.init_node("turtle_controller")

    # create a publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    # create a subscriber
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.loginfo("Node has been started")
    rospy.spin()