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
S = 128.
M_cr = 0.79

MTOW = 69000.*g
Mff_start = 0.99*0.99*0.995*0.98
Mff_end = 0.99*0.99*0.995*0.98*0.972
Wf_used_start = (1-Mff_start)*MTOW
Wf_used_end = (1-Mff_end)*MTOW

W_start = MTOW - Wf_used_start
W_end = MTOW - Wf_used_end
WS_start = W_start/S
WS_end = W_end/S

lambdac_0 = 0.68 #leading edge sweep
lambdac_4 = 0.66 #quarter chord sweep
lambdac_2 = 0.63 #half chord sweep

q_cr = cruise_q(h_cr)
V_cr = cruise_speed(h_cr)
a = a(h_cr)
M_low = 0.2
V_low = M_low*a

MAC = 3.77828726
nu =  8.73*10**(-6)            #kinematic viscosity at T = 216.6499 K
mu = 14.21*10**(-6) 
mu_to = 18.03E-6
rho_cr = ISA(h_cr)[2]
rho0 = 1.225
Re = (V_cr*cos(lambdac_0)*rho_cr*MAC)/mu                 #Reynolds number
Re_low = (V_low*cos(lambdac_0)*rho_cr*MAC)/mu


A = 14.
beta = np.sqrt(1-M_cr*M_cr)
eta = 0.95  #airfoil eff factor



CL_des = 1.1*(1/q_cr)*(0.5*(WS_start+WS_end))    #design lift coeffcient of the wing
Cl_des = CL_des/(cos(lambdac_0)*cos(lambdac_0))  #design lift coefficient of airfoil
Cl_des_M0 = Cl_des*np.sqrt(1-M_cr*M_cr)

CL_alpha = (2*pi*A)/(2+np.sqrt(4+(A*beta/eta)**2*(1+tan(lambdac_2)*tan(lambdac_2)/(beta*beta))))

print (CL_des)
print (Cl_des)
print (Re)
print (Cl_des_M0)
print (lambdac_0*180/pi)
#
CLmaxclmax = 0.52
dCL_max = -0.19
alpha_0L = -4.9     #alpha at L=0, follows from airfoil
Cl_max = 1.66      #follows from airfoil
alpha_trim =  CL_des/CL_alpha + alpha_0L #alpha at CL_des
#CL_max = CLmaxclmax*Cl_max + dCL_max
CL_max = 0.9*Cl_max*cos(lambdac_4)

print (CL_alpha)





