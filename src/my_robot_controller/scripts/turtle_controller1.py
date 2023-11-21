# all lines on right will be in Red color and Left side will be in green color

#! /usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

previous_x = 0

def call_set_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r, g, b, width, off)
        # rospy.loginfo(response)
    except rospy.ServiceException as e:
        print("Rospy Error: ", str(e))
        rospy.logwarn(e)
    except Exception as e:
        print("Error: ", str(e))

def pose_callback(pose):
    cmd = Twist()
    if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
        cmd.linear.x = 1.0
        cmd.angular.z = 1.4
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    
    global previous_x
    # we need to limit the service call
    if pose.x > 5.5 and previous_x < 5.5:
        # previous_x = pose.x
        rospy.loginfo("Setting color to green")
        call_set_pen_service(0,255,0, 3, 0)
    elif pose.x < 5.5 and previous_x > 5.5:
        # previous_x = pose.x
        rospy.loginfo("Setting color to red")
        call_set_pen_service(255, 0, 0, 3, 0)
    # else:
    #     call_set_pen_service(255, 0, 0, 3, 0)
    previous_x = pose.x
    pub.publish(cmd)

if __name__ == '__main__':

    rospy.init_node("turtle_controller")
    rospy.wait_for_service("/turtle1/set_pen") # wait for service to UP
    call_set_pen_service(255, 0, 0, 3, 0) # set Red color
    # create a publisher
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    # create a subscriber
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    rospy.loginfo("Node has been started")
    rospy.spin()