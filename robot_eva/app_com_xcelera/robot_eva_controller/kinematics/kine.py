import roboticstoolbox as rtb
import numpy as np
from math import pi




class Kine:

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0
        self.zero = 0.0
        #Create robot
        self.eva = rtb.models.DH.EVA()
        #start axes
        self.eva.q = self.eva.qr
        #define
        self.dg = pi/180
        self.rad = 180/pi

    def apply_f_kinematics(self):
        q = [self.zero,self.zero,self.zero,self.zero,self.zero]
        T = self.eva.fkine(q)
        print(T)

    def apply_inv_kinematics(self,pos_x,pos_y,pos_z):
        pos_desired = [pos_x,pos_y,pos_z]
        #matriz R
        R = np.array([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])
        T_desired = np.eye(4) #4*4
        T_desired[:3,:3] = R
        T_desired[:3, 3] = pos_desired
        Ti = self.eva.ik_LM(T_desired) #cinematica inversa a la matriz T deseada

        # from rad to degree
        for j in range(5):
            Ti[0][j] = (Ti[0][j])*(180/pi)

        print(Ti[0])

    def path_plannig(self,pos_start,target,steps):

        pos_start[0] = pos_start[0]*(-1)
        pos_start[3] = pos_start[3]*(-1)
        pos_start[4] = pos_start[4]*(-1)

        target[0] = target[0]*(-1)
        target[3] = target[3]*(-1)
        target[4] = target[4]*(-1)

        qt = rtb.tools.trajectory.jtraj(pos_start,target,steps)
        result = list()
        for j in qt.q:
            result.append(j)

        return result






