#!/usr/bin/env python3

import rospy
from ros_trajectory_planner.srv import *
from ros_trajectory_planner.msg import cubic_traj_params
from ros_trajectory_planner.msg import cubic_traj_coeffs


def callback(data):
    #publishing the initialised service
    pub = rospy.Publisher('coeffs', cubic_traj_coeffs, queue_size=0)

    try:
        #trying to connect to the 'compute_cubic_traj' service
        compute = rospy.ServiceProxy('compute_srv', compute_cubic_traj)
        #computing tajectories using teh data from the subscriber if service connects
        resp = compute(data)
        #constructing the message 
        msg = cubic_traj_coeffs()
        #addigning the values from the topic to the service
        msg.a0 = resp.a0
        msg.a1 = resp.a1
        msg.a2 = resp.a2
        msg.a3 = resp.a3
        msg.t0 = data.t0
        msg.tf = data.tf
        #publishing the data
        print(msg)
        pub.publish(msg)
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)


def cubic_traj_planner():
    #initialising the node
    rospy.init_node('cubic_traj_planner', anonymous=True)
    #waiting for the service to start
    rospy.wait_for_service('compute_srv')
    #subscribe to the 'cubic_traj_params' topic and send the data to callback
    rospy.Subscriber('points', cubic_traj_params, callback)
    #spin to keep alive
    rospy.spin()

if __name__ == "__main__":
    cubic_traj_planner()
