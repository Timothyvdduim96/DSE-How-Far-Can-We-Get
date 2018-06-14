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

g = value("g")
S = value('S')
M_cr = value("M_cr")
A = value("A")
taper = value("taper")
h_cr = value("h_cr")
h_low = 0.

MTOW = value("MTOW")*g
Mff_start = 0.99*0.99*0.995*0.98
Mff_end = 0.99*0.99*0.995*0.98*0.972
Wf_used_start = (1-Mff_start)*MTOW
Wf_used_end = (1-Mff_end)*MTOW

W_start = MTOW - Wf_used_start
W_end = MTOW - Wf_used_end
WS_start = W_start/S
WS_end = W_end/S

lambdac_0 =  value('lambdac_0') #leading edge sweep
a_cr = a(h_cr)
rho_cr = 
q_cr = 0.5 * rho_cr * value('v_cr')**2
V_cr = M_cr * a_cr


MAC = value("MAC")
nu =  8.73*10**(-6)            #kinematic viscosity at T = 216.6499 K
mu = 14.21*10**(-6)
rho_cr = value("rho_cr")
rho0 = value("rho_0")

#Clean cruise conditions with cruise Reynold's number
beta_cruise = np.sqrt(1-M_cr*M_cr)

#Re_cr = (V_cr * cos(lambdac_0) * rho_cr * MAC) / mu                 #Reynolds number
CL_des_cruise_clean_plane = (1/q_cr)*(0.5*(WS_start+WS_end)) #design lift coefficient of the entire aircraft
CL_des_cruise_clean_wing = 1.1*(1/q_cr)*(0.5*(WS_start+WS_end))    #design lift coeffcient of the wing
Cl_des_cruise_clean = CL_des_cruise_clean_wing/(cos(lambdac_0)*cos(lambdac_0))  #design lift coefficient of airfoil
Cl_des_M0 = Cl_des_cruise_clean*np.sqrt(1-M_cr*M_cr)

#Airfoil parameters
eta_airfoil = 0.95  #airfoil eff factor
Cl_max_cruise_clean = 2.363
Cd_min_cruise_clean = 0.006
Cm_des_cruise_clean = -0.116
alpha_des_cruise_clean = 1.36 *pi /180               #rad
M_crit_cruise_clean = 0.663
alpha_0L_cruise_clean = -3.82 *pi /180               #rad

lambdac_LE = acos(M_crit_cruise_clean/M_cr)
lambdac_2 = atan(tan(lambdac_LE) - (4/A)*(0.5*(1-taper)/(1+taper)))
lambdac_4 = atan(tan(lambdac_LE) - (4/A)*(0.25*(1-taper)/(1+taper)))

CL_alpha_cruise_clean = (2*pi*A)/(2+np.sqrt(4+(A*beta_cruise/eta_airfoil)**2*(1+tan(lambdac_2)*tan(lambdac_2)/(beta_cruise*beta_cruise))))
alpha_trim_cruise_clean =  CL_des_cruise_clean_wing/CL_alpha_cruise_clean + alpha_0L_cruise_clean   #alpha at CL_des in rad

CL_max_cruise_clean_wing = 0.52 * Cl_max_cruise_clean -0.19
CL_max_cruise_clean_plane = CL_max_cruise_clean_wing /1.1
# CL_max_cruise_clean_plane = 0.9*Cl_max_cruise_clean*cos(lambdac_4) /1.1
# CL_max_cruise_clean_wing = 0.9*Cl_max_cruise_clean*cos(lambdac_4)

alpha_stall_cruise_clean = (CL_max_cruise_clean_wing / CL_alpha_cruise_clean) + alpha_0L_cruise_clean + (4 * pi /180) #rad



#take-off/land clean conditions
M_low = 0.2
a_low = a(h_low)
V_low = M_low * a_low
mu_low = 1.798*10**(-5)
beta_low = np.sqrt(1-M_low*M_low)
rho_low = rho0
Re_low = (V_low*cos(lambdac_LE)*rho_low*MAC)/mu_low                 #Reynolds number

Cl_max_low_clean = 2.3
Cd_min_low_clean = 0.005
Cp_min_low_clean = -1.314
M_crit_low_clean = 0.645
alpha_0L_low_clean = np.radians(-3.82)              #rad

CL_alpha_low_clean = (2*pi*A)/(2+np.sqrt(4+(A*beta_low/eta_airfoil)**2*(1+tan(lambdac_2)*tan(lambdac_2)/(beta_low**2))))

CL_max_low_clean = 0.9*Cl_max_low_clean*cos(lambdac_4)

alpha_stall_low_clean = (CL_max_low_clean / CL_alpha_low_clean) + alpha_0L_low_clean + (4 * pi /180)  #rad
#HLD requirements
CL_TO = 2.1
CL_land = 2.2

CL_0 = 0.31
dCL_HLD_TO = CL_TO - CL_max_low_clean
dCL_HLD_land = CL_land - CL_max_low_clean

#Take-off conditions


#Landing conditions

string_airfoil2 = ["V_cr", "eta_airfoil", "Cl_max_cruise_clean", "alpha_0L_low_clean", "CL_alpha_low_clean", "alpha_stall_low_clean", "Cd_min_cruise_clean", "Cm_des_cruise_clean", "alpha_0L_cruise_clean", "alpha_des_cruise_clean", "alpha_stall_cruise_clean", "alpha_trim_cruise_clean", "CL_max_cruise_clean_plane", "CL_max_cruise_clean_wing", "CL_max_low_clean", "CL_alpha_cruise_clean", "Cd_min_low_clean", "M_crit_cruise_clean", "lambdac_LE", "lambdac_2", "lambdac_4", "dCL_HLD_land", "dCL_HLD_TO", 'CL_0']
