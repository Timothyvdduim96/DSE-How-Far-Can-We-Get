# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:44:33 2018

@author: mrvan
"""


from scipy.integrate import quad
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
from math import *
from parameters import *

c_r = value('c_r')
c_t = value('c_t')
b = value('b')
S = value('S')
V = value('V_cr')
c_a_c = 0.2
c_l_alpha =  6.548  #lift slope of the airfoil [rad]
tau = 0.4      #aileron effectiveness with c_a/c = 0.2
c_d0 = 0.006
da = 20*pi/180.         #aileron deflection [rad]
dphi = 45 * pi/180. #roll angle required

a1 = c_r   
a2 = (c_r-c_t)/(0.5*b)



b1 = 0.79*(b/2) #inboard spanwise posisition aileron
b2 = 0.95*(b/2) #outnboard spanwise position aileron

ba_i = b1
ba_o = b2

integral1 = 0.5*a1*b2**2-(1/3.)*a2*b2**3 - 0.5*a1*b1**2 + (1/3.)*a2*b1**3
C_l_da = (2*c_l_alpha*tau*integral1)/(S*b) #aileron control derivative

integral2 = (1/3.)*a1*(b/2.)**3 - (1/4.)*a2*(b/2.)**4
C_l_p = (-4*(c_l_alpha + c_d0)*integral2)/(S*b*b)

c_a1 = (a1-a2*b1)*c_a_c #chord of aileron
c_a2 = (a1-a2*b2)*c_a_c

S_a = 0.5*(c_a2+c_a1)*(b2-b1) #aileron area

P = -(C_l_da/C_l_p)*da*(2*V/b)
dt = dphi/P


string_ailerons = ['S_a','ba_i','ba_o']



