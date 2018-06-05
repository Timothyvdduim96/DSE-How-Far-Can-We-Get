# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 12:06:51 2018

@author: mrvan
"""

__author__ = 'Menno vd Toorn'
from scipy.integrate import quad
from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from math import *
from parameters import *

g = 9.80665

WS_start = 5302.
WS_end = 5302.

q_cr = cruise_q(h_cr)
V_cr = cruise_speed(h_cr)
MAC = 3.77828726
nu =  8.73*10**(-6)            #kinematic viscosity at T = 216.6499 K
Re = (V_cr*MAC)/nu                 #Reynolds number



lambdac_0 = 0.68

CL_des = 1.1*(1/q_cr)*(0.5*(WS_start+WS_end))    #design lift coeffcient of the wing
Cl_des = CL_des/(cos(lambdac_0)*cos(lambdac_0))  #design lift coefficient of airfoil

print (CL_des)
print (Cl_des)
print (Re)
print (V_cr)