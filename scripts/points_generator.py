#!/usr/bin/env python3

import rospy
import random
from ros_trajectory_planner.msg import cubic_traj_params

def points_generator():
    #initialising the new topic: points that will publish the trajectory parameters
    pub = rospy.Publisher('points', cubic_traj_params, queue_size=0)
    #initialising the new node
    rospy.init_node('points_generator', anonymous=True)
    #setting the rate to fire once every 20 seconds
    rate = rospy.Rate(1/20)
    #constructing the message
    msg = cubic_traj_params()
    #while rospy is runningm generate random numbers to populate the values given the parameters from the PDF
    while not rospy.is_shutdown():
        # generate random numbers
        msg.p0 = random.uniform(-10, 10)
        msg.pf = random.uniform(-10, 10)
        msg.v0 = random.uniform(-10, 10)
        msg.vf = random.uniform(-10, 10)
        msg.t0 = 0
        #this format was causing errors
        #dt = random.uniform(5, 10)
        #msg.tf = msg.t0 + dt
        msg.tf = msg.t0 + round(random.uniform(5, 10))
        #logging and publishind the message
        rospy.loginfo(msg)
        pub.publish(msg)
        print(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        points_generator()
    except rospy.ROSInterruptException:
        pass
