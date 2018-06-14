# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:12:26 2018

@author: mrvan
"""

from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy.optimize import fsolve


S = value('S')
A = value('A')
b = value('b')
taper = value('taper')
c_r = value('c_r')
c_t = value('c_t')
lambdac_LE = value('lambdac_LE')
r_fus = value('d_ext_fus')/2.

a1 = c_r   
a2 = (c_r-c_t)/(0.5*b)

CL_max_low_clean = value('CL_max_low_clean')

CL_to = 2.1
CL_land = 2.5


dC_L_max_to = CL_to - CL_max_low_clean + 0.2
dC_L_max_land =  CL_land - CL_max_low_clean + 0.3



lambda_hingeline_flap = atan(tan(lambdac_LE) - (4/A)*(1*(1-taper)/(1+taper)))
lambda_hingeline_slat = lambdac_LE


d_f_land = 40 #deg flap deflection at landing
d_f_to = 15 #deg flap deflection at take-off


dc_cf_land = 0.6 #single slotted (0.8 for double slotted)
dc_cf_to = 0.5 #single slotted (0.6 for double slotted)

cf_c = 0.35 #flap chord/wing chord for slotted flaps
cs_c = 0.15 #slat chord/wing chord (sforza)

c_ext_c_land = 1 + cf_c * dc_cf_land #extended chord divided by chord during landing
c_ext_c_to = 1 + cf_c * dc_cf_to #extended chord divided by chord during take-off
c_ext_c_slat = 1.092 #from sforza

dC_l_max_flap = 1.3 * c_ext_c_land  #for single slotted fowler flap (1.6 for double slotted)
dC_l_max_slat = 0.3 * c_ext_c_slat 



Swf_land_TE = (0.85*dC_L_max_land*S)/(0.9*dC_l_max_flap*cos(lambda_hingeline_flap))
Swf_to_TE = (0.9*dC_L_max_to*S)/(0.9*0.7*dC_l_max_flap*cos(lambda_hingeline_flap))
Swf_TE = max([Swf_land_TE,Swf_to_TE])


Swf_land_LE = (0.15*dC_L_max_land*S)/(0.9*dC_l_max_slat*cos(lambda_hingeline_slat))
Swf_to_LE = (0.1*dC_L_max_land*S)/(0.9*0.7*dC_l_max_slat*cos(lambda_hingeline_slat))
Swf_LE = max([Swf_land_LE,Swf_to_LE])

dalpha_0l_airfoil_land = -15 #deg
dalpha_0l_airfoil_to = -10 #deg

dalpha_0L_land = dalpha_0l_airfoil_land*(Swf_TE/S)*cos(lambda_hingeline_flap)#deg
dalpha_0L_to = dalpha_0l_airfoil_to*(Swf_TE/S)*cos(lambda_hingeline_flap) #deg

CL_alpha_low_clean = value('CL_alpha_low_clean')* pi/180. #per deg
S_ext_S_land = 1 + (Swf_TE/S)*(c_ext_c_land-1)
S_ext_S_to   = 1 + (Swf_TE/S)*(c_ext_c_to-1)
S_ext_S_slat  = 1 + (Swf_LE/S)*(c_ext_c_slat-1)

CL_alpha_flapped_land = S_ext_S_land * CL_alpha_low_clean #per deg
CL_alpha_flapped_slatted_land = S_ext_S_slat * CL_alpha_flapped_land
CL_alpha_flapped_to = S_ext_S_to * CL_alpha_low_clean #per deg
CL_alpha_flapped_slatted_to = S_ext_S_slat * CL_alpha_flapped_to

alpha_0L_low_clean = value('alpha_0L_low_clean')* 180./pi
alpha = np.arange(-10.,25.,0.1)

C_L_curve_clean = CL_alpha_low_clean*(alpha - alpha_0L_low_clean)
C_L_curve_land = CL_alpha_flapped_slatted_land*(alpha - alpha_0L_low_clean - dalpha_0L_land)
C_L_curve_to = CL_alpha_flapped_slatted_to*(alpha - alpha_0L_low_clean - dalpha_0L_to)

alpha_stall_low_clean = value('alpha_stall_low_clean')*180./pi #deg 


CL_land = CL_land
CL_max_land = CL_max_low_clean + dC_L_max_land
CL_land_margin = CL_max_land 
alpha_stall_flapped_land = (CL_land_margin/ CL_alpha_flapped_slatted_land) + alpha_0L_low_clean + dalpha_0L_land +  4 


CL_to = CL_to
CL_max_to = CL_max_low_clean + dC_L_max_to
CL_to_margin = CL_max_to 
alpha_stall_flapped_to = (CL_to_margin / CL_alpha_flapped_slatted_to) + alpha_0L_low_clean + dalpha_0L_to +  4 


plt.subplot(221)
plt.plot(alpha,C_L_curve_clean,label='clean')
plt.plot(alpha_stall_low_clean,CL_max_low_clean, marker = 'o', label = 'stall clean')
plt.plot(alpha,C_L_curve_land,label='land')
plt.plot(alpha_stall_flapped_land,CL_land_margin, marker = 'o', label = 'stall flapped')
plt.plot([-10,25],[CL_land,CL_land])
plt.grid(True)
plt.legend(loc='upper left')
plt.ylabel("C_L")
plt.xlabel("alpha [deg]")
plt.title("C_L - alpha curve")

plt.subplot(222)
plt.plot(alpha,C_L_curve_clean,label='clean')
plt.plot(alpha_stall_low_clean,CL_max_low_clean, marker = 'o')
plt.plot(alpha,C_L_curve_to, label='take-off')
plt.plot(alpha_stall_flapped_to,CL_to_margin, marker = 'o')
plt.plot([-10,25],[CL_to,CL_to])
plt.grid(True)
plt.legend(loc='upper left')
plt.ylabel("C_L")
plt.xlabel("alpha [deg]")
plt.title("C_L - alpha curve")
plt.show()

S_flapped_land = S*(S_ext_S_land)
S_flapped_to = S*(S_ext_S_to)
S_slatted = S*(S_ext_S_slat)

S_flaps_land = S_flapped_land - S
S_flaps_to = S_flapped_to - S
S_slats = S_slatted - S

bf_i = r_fus  #inboard flap position
func = lambda x : (x-bf_i)*(2*a1-a2*bf_i-a2*x) - Swf_TE
bf_o_init = 6
bf_o = fsolve(func, bf_o_init )[0]  #outboard flap position

bs_i = r_fus + 2 #inboard slat position
func2 = lambda x2 : (x2-bs_i)*(2*a1-a2*bs_i-a2*x2) - Swf_LE
bs_o_init = 6
bs_o = fsolve(func2, bs_o_init )[0]  #outboard slat position

bf_i_perc = bf_i/(b/2.)
bf_o_perc = bf_o/(b/2.)
bs_i_perc = bs_i/(b/2.)
bs_o_perc = bs_o/(b/2.)

print (bf_i_perc)
print (bf_o_perc)
print (bs_i_perc)
print (bs_o_perc)




string_HLD = ['Swf_LE','Swf_TE','S_flaps_land','S_flaps_to','S_slats','bs_i','bs_o','bf_i','bf_o','d_f_land','d_f_to','c_ext_c_land','c_ext_c_to','cf_c','cs_c']

