#!/usr/bin/env python3

import rospy
from ros_trajectory_planner.msg import cubic_traj_coeffs
from ros_trajectory_planner.msg import pos_traj
from ros_trajectory_planner.msg import vel_traj
from ros_trajectory_planner.msg import acc_traj


def callback(data):
    #publishing the initialised messages to topics
    acc_pub = rospy.Publisher('acc_traj', acc_traj, queue_size=0)
    pos_pub = rospy.Publisher('pos_traj', pos_traj, queue_size=0)
    vel_pub = rospy.Publisher('vel_traj', vel_traj, queue_size=0)    
  
    #initialising the messages
    acc_msg = acc_traj()
    pos_msg = pos_traj()    
    vel_msg = vel_traj()    

    #calculating acceleration, position & velocity trajectories
    acc_msg.trj = 2 * data.a2 + 6 * data.a3 * data.tf
    pos_msg.trj = data.a0 + data.a1 * data.tf + data.a2 * (data.tf**2) + data.a3 * (data.tf**3)
    vel_msg.trj = data.a1 + 2 * data.a2 * data.tf + 3 * data.a3 * (data.tf**2)
    
    #publishing the messages 
    print('Acceleration trajectory: %d, Position trajectory: %d, Velocity trajectory: %d' % (acc_msg.trj, pos_msg.trj, vel_msg.trj))
    acc_pub.publish(acc_msg)
    pos_pub.publish(pos_msg)
    vel_pub.publish(vel_msg)

def plot_cubic_traj():
    #initialising the node
    rospy.init_node('plot_cubic_traj', anonymous=True)
    #subscribing to the 'cubic_traj_params' topic and sending the data to callback
    rospy.Subscriber('coeffs', cubic_traj_coeffs, callback)
    #spin to keep alive
    rospy.spin()

if __name__ == "__main__":
    try:
        plot_cubic_traj()
    except rospy.ROSInterruptException:
        pass
