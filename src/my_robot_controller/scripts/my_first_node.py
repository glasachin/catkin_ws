#! /usr/bin/env python3

import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")

    rospy.loginfo("Hello! from test node")
    rospy.logwarn("This is a warning")
    rospy.logerr("This is an error")
    
    rospy.sleep(1)

    rospy.loginfo("End of program")

    # Run something for some thime at an rate of 10Hz
    rospy.loginfo("Test node has been started.")
    rate = rospy.Rate(10) # providing 10Hz rate

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()    # sleep for 0.1s i.e. 10Hz