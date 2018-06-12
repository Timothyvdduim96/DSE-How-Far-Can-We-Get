# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:12:26 2018

@author: mrvan
"""

from scipy.integrate import quad
from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from math import *

S = value('S')
dC_L_max_to = value('dCL_HLD_TO')
dC_L_max_land =  value('dCL_HLD_land')

lambda_hingeline = 0





d_f_land = 50 #deg flap deflection at landing
d_f_to = 20 #deg flap deflection at take-off

dc_cf_land = 0.7 #single slotted (0.9 for double slotted)
dc_cf_to = 0.5 #single slotted (0.6 for double slotted)

cf_c = 0.35 #flap chord/wing chord for slotted flaps
c_ext_c_land = 1 + cf_c * dc_cf_land
c_ext_c_to = 1 + cf_c * dc_cf_to

dC_l_max_flap = 1.3 * c_ext_c_land  #for single slotted fowler flap (1.6 for double slotted)
dC_l_max_slat = 0.4 * c_ext_c_land

dC_l_max_land = dC_l_max_flap #+ dC_l_max_slat
dC_l_max_to = 0.7*(dC_l_max_flap) #+ dC_l_max_slat)


Swf_land = (dC_L_max_land*S)/(0.9*dC_l_max_land*cos(lambda_hingeline))
Swf_to = (dC_L_max_to*S)/(0.9*dC_l_max_to*cos(lambda_hingeline))
Swf_TE = max([Swf_land,Swf_to])

dalpha_0l_airfoil_land = -15 #deg
dalpha_0l_airfoil_to = -10 #deg

dalpha_0L_land = dalpha_0l_airfoil_land*(Swf_TE/S)*cos(lambda_hingeline)
dalpha_0L_to = dalpha_0l_airfoil_to*(Swf_TE/S)*cos(lambda_hingeline)

CL_alpha_low_clean = value('CL_alpha_low_clean')
S_ext_S_land = 1 + (Swf_TE/S)*(c_ext_c_land-1)
S_ext_S_to   = 1 + (Swf_TE/S)*(c_ext_c_to-1)

CL_alpha_flapped_land = S_ext_S_land * CL_alpha_low_clean
CL_alpha_flapped_to = S_ext_S_to * CL_alpha_low_clean

print (CL_alpha_low_clean)
print (CL_alpha_flapped_land)