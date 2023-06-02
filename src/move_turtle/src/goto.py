#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odemetry
from math import pow,atan2, sqrt

rospy.init_node('move_turtle')
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
odom_subscriber = rospy.Subscriber('/odom', Odometry, callback)
n_cycles=rospy.get_param('~n_cycles',1)# get number of cycles from parameter server

def callback(data):
if _name_ == '_main_':
    try:
        # Define the three points of the cycle
        points = [(3.0278525352478027, -1.4700452089309692), (8.72671127319336, -2.4896795749664307), (4.081020355224609, -2.7720134258270264)]
        for _ in range(n_cycles): #iterate over the specified number of cycles for point in points
        goto_point(point[0],point[1])
        rospy.sleep(1) #DELAY between points
        except rospy.ROSInterruptException:
        pass

        while not rospy.is_shutdown():
            for point in points:
                goto_point(point[0], point[1])
                rospy.sleep(1)  # Delay between points

    except rospy.ROSInterruptException:
        pass
	
