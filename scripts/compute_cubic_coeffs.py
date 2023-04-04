#!/usr/bin/env python3

import rospy
import numpy as np
from ros_trajectory_planner.srv import *

def handle_service(req):
    #creating the matricies
    params = req.params
    print('Accepting request!')
    matrix1 = np.matrix('1 %d %d %d; 0 1 %d %d; 1 %d %d %d; 0 1 %d %d' % (params.t0, params.t0**2, params.t0**3, 2*params.t0, 3*(params.t0**2), params.tf, params.tf**2, params.tf**3, 2*params.tf, 3*(params.tf**2)))

    matrix2 = np.matrix('%d %d %d %d' % (params.p0, params.v0, params.pf, params.vf))
    #multiplying the inverse of matrix 1 by matrix 2
    matrix3 = matrix2 * matrix1.getI()
    #converting the matrix into a list to get the values
    result = matrix3.getA1().tolist()
    print('Returning %s' % result)
    return compute_cubic_trajResponse(result[0], result[1], result[2], result[3])

def compute_cubic_coeffs():
    #initialising the node 
    rospy.init_node('compute_cubic_coeffs')
    #initialising the service 'compute cubic traj' to get the data and pass it to handle_service
    s = rospy.Service('compute_srv', compute_cubic_traj, handle_service)
    print("Ready to compute!")
    #spin to keep alive
    rospy.spin()

if __name__ == "__main__":
    compute_cubic_coeffs() 
