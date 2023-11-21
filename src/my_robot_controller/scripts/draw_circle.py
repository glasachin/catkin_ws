#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("Draw_circle")
    rospy.loginfo("Node has been started")

    # Create a Publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10) # we are assigning a topic. Turtle sim topic for example simulation purpose.

    rate = rospy.Rate(2)    
    while not rospy.is_shutdown():
        # publish cmd velocity

        msg = Twist()   #create message
        msg.linear.x = 2.0
        msg.angular.z = 1.0    #because 2-D so not angular x and y
        
        # publish the message
        pub.publish(msg)

        # to keep rate
        rate.sleep()