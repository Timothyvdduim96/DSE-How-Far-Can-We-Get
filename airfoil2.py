# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 12:06:51 2018

@author: mrvan
"""

__author__ = 'Menno vd Toorn'
#from scipy.integrate import quad
#from scipy import optimize as opt
#import numpy as np
#import matplotlib.pyplot as plt
import math
from parameters import *

#aircraft parameters

g = 9.80665
S = 128.
M_cr = 0.79
A = 14.
taper = 0.27
h_cr = 11887.2

MTOW = 68731.*g
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



MAC = 3.77828726
nu =  8.73*10**(-6)            #kinematic viscosity at T = 216.6499 K
mu = 14.21*10**(-6)
rho_cr = ISA(h_cr)[2]
rho0 = 1.225

#Clean cruise conditions with cruise Reynold's number
beta_cruise = np.sqrt(1-M_cr*M_cr)
rho_cr = ISA(h_cr)[2]
Re = (V_cr*cos(lambdac_0)*rho_cr*MAC)/mu                 #Reynolds number

CL_des_cruise_clean = 1.1*(1/q_cr)*(0.5*(WS_start+WS_end))    #design lift coeffcient of the wing
Cl_des_cruise_clean = CL_des_cruise_clean/(cos(lambdac_0)*cos(lambdac_0))  #design lift coefficient of airfoil
Cl_des_M0 = Cl_des_cruise_clean*np.sqrt(1-M_cr*M_cr)
#Airfoil parameters
eta = 0.95  #airfoil eff factor
Cl_max_cruise_clean = 1.66
Cd_min_cruise_clean = 0.005
Cm_des_cruise_clean = -0.122
alpha_des_cruise_clean = 0.4                 #rad
M_crit_cruise_clean = 0.621
alpha_0L_cruise_clean = -4.9                  #rad

lambdac_0 = acos(M_crit_cruise_clean/M_cr)
lambdac_2 = atan(tan(lambdac_0) - (4/A)*(0.5*(1-taper)/(1+taper)))
lambdac_4 = atan(tan(lambdac_0) - (4/A)*(0.25*(1-taper)/(1+taper)))

CL_alpha_cruise_clean = (2*pi*A)/(2+np.sqrt(4+(A*beta_cruise/eta)**2*(1+tan(lambdac_2)*tan(lambdac_2)/(beta_cruise*beta_cruise))))
alpha_trim_cruise_clean =  CL_des_cruise_clean/CL_alpha_cruise_clean + alpha_0L_cruise_clean   #alpha at CL_des in rad

CL_max_cruise_clean = 0.9*Cl_max_cruise_clean*cos(lambdac_4)

alpha_stall_cruise_clean = (CL_max_cruise_clean / CL_alpha_cruise_clean) + alpha_0L_cruise_clean + (4 * pi /180) #rad

#take-off/land clean conditions
M_low = 0.2
h_low = 0.
a_low = a(h_low)
V_low = M_low*a_low
mu_low = 1.798*10**(-5)
beta_low = np.sqrt(1-M_low*M_low)
rho_low = rho0
Re_low = (V_low*cos(lambdac_0)*rho_low*MAC)/mu_low                 #Reynolds number
print V_low
print Re_low
# CL_des_low_clean =
# Cl_max_low_clean =
# Cd_min_low_clean =
# Cm_des_low_clean =
# alpha_des_low_clean =                     #rad
# M_crit_low_clean =
# alpha_0L_low_clean =                      #rad
#
# CL_alpha_low_clean = (2*pi*A)/(2+np.sqrt(4+(A*beta_low/eta)**2*(1+tan(lambdac_2)*tan(lambdac_2)/(beta_low*beta_low))))
# alpha_trim_low_clean =  CL_des_low_clean/CL_alpha_low_clean + alpha_0L_low_clean   #alpha at CL_des in rad
#
# CL_max_low_clean = 0.9*Cl_max_low_clean*cos(lambdac_4)
#
# alpha_stall_low_clean = (CL_max_low_clean / CL_alpha_low_clean) + alpha_0L_low_clean + (4 * pi /180) #rad
#
# #HLD requirements
# CL_TO =
# CL_land =
#
#
# dCL_HLD_TO = CL_TO - CL_max_low_clean
# dCL_HLD_land = CL_land - CL_max_low_clean
#
# #Take-off conditions
#
#
# #Landing conditions