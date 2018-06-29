# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:35:54 2018

@author: helua
"""

#-------Engine noise
from math import *
from parameters import ISA

#atmospheric properties
alt = 11000.
dens_0 = 1.225 #ambient density
dens_amb = ISA(alt)[1]
Temp0 = ISA(alt)[0]
Temp = ISA(alt)[0]
a_amb0 = sqrt(1.4*287*Temp0)
a_amb = sqrt(1.4*287*Temp)

theta = radians(90) #polar angle

#engine characteristics:
v_9 = 31. #exhaust jet velocity
v_19 = 301.
v_m = 233.08 #mean inflow velocity
v_9_eff = v_9*(1-((v_m/v_9)*cos(theta)))**(2/3) #effective jet speed
rho_9 = 0.048#density at point 9
A9 =  0.785 #nozzle area
D9 = 1. #nozzle diameter
A19 = 2.35
T_t2 = 242
T_t9 = 778.
T_t19 = 226.
T_tamb = 216.65
T9ratio = T_t9/T_tamb
eta_is = 0.9 #isentropic efficiency
PressRatio_t2_13 = 1.4
K = 1.4
massflow_ref =  0.453 #kg/s
massflow = 550 #kg/s
#f_b = #blade passing frequency
d = 200. #observer distance
#calculations:
omega = ((3.0 *(v_9_eff/a_amb)**3.5)/(0.6+(v_9_eff/a_amb)**3.5)) - 1 #density exponentby Stone
Ma_con = 0.62*((v_9-(v_m*cos(theta)))/a_amb)

L_norm = 141. + 10*log(((dens_amb/dens_0)**2)*((a_amb/a_amb0)**4)) \
+ (10*log(A9/d**2)) + (10*omega*log(rho_9/dens_amb)) + (75*log(v_9_eff/a_amb)) \
- (15*log((1+(Ma_con*cos(theta)))**2)) + (0.04*Ma_con**2) \
- (10*log(1-(Ma_con*cos(theta)))) \
+ (3*log(((2*A9)/(pi*(D9)**2)) + 0.5))

#how to do this
f = 200
str9_param_1 = (1+(0.62*((v_9-v_m)/a_amb)*cos(theta)))**2 + (0.01538*((v_9-v_m)/a_amb)**2)
str9_param_2 = (1+(0.62*((v_9)/a_amb)*cos(theta)))**2 + (0.01538*((v_9)/a_amb)**2)
str9_param = (str9_param_1/str9_param_2)**0.5
Str_9 = f * (sqrt((4*A9)/pi)/v_9_eff) * ((D9/sqrt((4*A9)/pi))**0.4) * ((T9ratio)**(0.4*(1+cos(theta)))) \
* (1-(Ma_con*cos(theta))) * str9_param

if A19/A9 < 29.7:
    m = 1.1*sqrt(A19/A9)
else:
    m = 6.0
    
DL_ejet = (5*log(T_t9/T_t19)) + (10*log(((1-(v_19/v_9))**m)+(1.2*((1+(A19/A9)*(v_19**2/v_9**2))**4)/(1+(A19/A9))**3)))
f_freq = 0.1709*(log(1+(A19/A9)))**3 \
- (0.6335*(log(1+(A19/A9)))**2) + (1.1037*log(1+(A19/A9)))
Str_ejet = Str_9 * (1-f_freq*(0.5+(((T_t19*v_19*A19)/(T_t9*v_9*A9))/(1+((T_t19*v_19*A19)/(T_t9*v_9*A9)))))**2)
DL_dirspec = 
#jet noise final equation
L_jet = L_norm + DL_dirspec + DL_ejet


#-----Fan noise
DT_tref = 0.5555 K
DT_t2_13 = Tt,2 * 1/eta_is*((PressRatio_t2_13**((K-1)/K))-1)
L_norm_fan =  20*log(DT_t2_13/DT_tref) + 10*log(massflow/massflow_ref)

D_Lspec = 10*log(exp(-0.5*(log(frequency/(2.5*f_b))/log(2.2))**2))
DL_vel_bbn_in =    #value based on relative machnumber and relative machnumber for the design point on page 36
DL_dir = #directivity from ref 26 figure 7
L_bbn_in = L_norm_fan + DL_dir + D_Lspec + DL_vel_bbn_in
delta = abs(Ma_con/(1-(ns/nr))) #cutoff condition
DL_h = #level deltas page 37 
DL_vel_dtn_in = #velocity dependent term page 37
L_dtn_in = L_norm_fan + DL_vel_dtn_in + DL_dir + DL_h + cdist
L_ctn_in = 0 #The combination tone noise is 0 for the subsonic case p. 37
DL_vel_ex = #see equation from page 37
DL_dir_ex = #see ref 26 figure 7b
spacing_rss = #spacing between rotor and stator disc
c_ex = -5*log(1/3*spacing_rss)

L_bbn_ex = L_norm_fan + DL_vel_ex + DL_dir_ex + D_Lspec + c_ex

DL_vel_ex_dtn = #see part b page 39
DL_dir_ex_dtn = #see ref 26 page
DL_spec_ex_dtn = #see ref 26

L_dtn_ex = L_norm_fan + DL_vel_ex_dtn + DL_dir_ex_dtn + DL_spec_ex_dtn + c_ex



L_fan_in = L_norm_fan + L_bbn_in + L_dtn_in + L_ctn_in + c_in
L_fan_ex = L_norm_fan + L_bbn_ex + L_dtn_ex + c_in
L_fan_total = 10*log(10**(L_fan_in/10)+10**(L_fan_ex/10))

L_engine = 10*log(10**(L_fan_total/10)+10**(L_jet/10))


