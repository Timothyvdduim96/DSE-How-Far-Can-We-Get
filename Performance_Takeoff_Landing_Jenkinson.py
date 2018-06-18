# -*- coding: utf-8 -*-
"""
Created on Fri Jun 08 14:29:49 2018

@author: helua
"""

from math import *
from parameters import ISA
import numpy as np
import matplotlib.pyplot as plt
#----- constants
g = 9.80665
MTOW = 68731. *g #68731
mu_roll = 0.02
mu_brake = 0.4
#alt = raw_input("Input the altitude of the airport in meters:")
#alt = eval(alt)
S = 110.  
A = 14.
thrust = 213000.
oswald = 0.7276
gamma_climb = radians(3.)
gamma_land = radians(3.)
h_scr = 15.24 #screen height in m change to 15.24
h_scr_to = 11 #screen height for take-off CS 21.107
lamda = 14. #bypass ratio
CL_max_to = 1.9
CL_to = 0.6 #takeoff cl during ground roll
CD0_to = 0.04
CD0_climb = 0.06
CL_max_land = 2.5
CD0_land = 0.06
MLW = MTOW - (0.67*9500*9.80665)
n_land = 1.2
P_0 = ISA(0)[1]
T_0 = 288.15
#------ ground roll
takeoff_distances = []
landing_distances = []
altitude = []

A_eng = 3.1196
V_eng = 132.39
Vj = 400

for alt in range(0,1500,100):
    dens = ISA(alt)[2]
    Temp = ISA(alt)[0]
    P_alt = ISA(alt)[1]
    V_min_to = sqrt((MTOW/S)*(2/dens)*(1/CL_max_to))
    V_LOF = V_min_to*1.1
    a = sqrt(1.4*287*Temp)
    M_takeoff = (V_LOF*0.707)/a
    V_TRANS =1.15 *V_min_to
    V2 = V_min_to*1.2
    
    #CD_to = 0.035 + 0.05*(CL_to**2)
    CD_to = CD0_to + (CL_to)**2/(pi*A*oswald)
    ratio_net_to_static = (1-(2*(M_takeoff*((1+lamda)/(3+2*lamda))))) #from CADP p. 412 chapter 10, Jenkinson suggests using 0.864
    #ratio_net_to_static = 0.864
    ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.5)*M_takeoff) + ((0.23+(0.19*sqrt(lamda)))*M_takeoff**2)   #paper voskuijl
    ratio = (P_alt/P_0) *sqrt(T_0/Temp)      #effect of altitude based on thrust  
    K_T = (ratio_net_to_static*thrust*ratio/MTOW)-mu_roll
    K_A = dens/((2*MTOW)/S)*(-CD_to+(mu_roll*CL_to))
    
    x_groundrun = (1/(2*g*K_A))*log((K_T+(K_A*V_LOF**2))/K_T)
    
    
    #-------Transition to climb
    n = 1.2 #loadfactor climb 
    r = 7380/(g*(n-1)) #m
    
    #------Final climb gradient
    CL_climb = CL_max_to/(1.2)**2
    
    CD_climb = CD0_climb + (CL_climb)**2/(pi*A*oswald)
    
    #CD_climb = 0.025 + 0.05*(CL_climb**2) #CD gear up, takeoff flaps
    D_climb = 0.5 * dens * (V2**2) * S * CD_climb
    climb_gradient = (0.803*thrust - D_climb)/(MTOW)
    x_transition = r * climb_gradient 
    
    h_T = r*climb_gradient *(climb_gradient/2) #altitude at end of transition
    screenmet = ""
    x_climb = (h_scr_to - h_T) / tan(gamma_climb)
    x_screen = ((r+h_scr_to)**2 - r**2)**0.5
    x_total_takeoff = 1.15*(x_groundrun + x_screen)
    
    if h_T <= h_scr_to:
        screenmet = "below the screenheight"   
    else:
        screenmet = "above the screenheight"
    if alt ==0:
        
        
        print "The groundrun distance is:", x_groundrun, "m"
        print "The distance to reach the screen height is:", x_screen, "m"
        print "The distance reached during transition is:", x_transition, "m"
        print "The altitude reached during transitions is", h_T, "m", "which is",screenmet
        print "The takeoff distance is", x_total_takeoff, "m"
        
        Af = 2.0 #fan diameter
        CD_failedengine = 0.3*Af/S
        CD_trim = 0.05*CD_climb
        CD_secondsegmentclimb = CD_climb + CD_failedengine +CD_trim
        D_secondsegmentclimb = 0.5*dens * (V2)**2 *S * CD_secondsegmentclimb
        climb_gradient_secondsegment_OEI = ((0.5*ratio_speed*thrust) - D_secondsegmentclimb)/(MTOW)
        
        if climb_gradient_secondsegment_OEI >= 0.024:
            print "V - The climb gradient requirement for OEI during the second segment of climb is MET!"
        else:
            print "X - The climb gradient requirement for OEI during the second segment of climb is NOT MET!"

        
    takeoff_distances.append(x_total_takeoff)
    altitude.append(alt)
    
    #----landing performance
    V_min_land = sqrt((MLW/S)*(2/dens)*(1/CL_max_land))
    V_F = (1.15+1.3)*V_min_land/2
    V_TD = 1.15*V_min_land
    r_land = V_F**2/(9.80665*(n_land-1.))
    h_F = (r_land*gamma_land*gamma_land)/2.
    s_A = (h_scr-h_F)/tan(gamma_land) #approach distance
    s_F = r_land * gamma_land #flare distance
    s_FR = 2*V_TD  #free roll distance
    print "Approach speed is:", V_min_land*1.3
    K_T_land = -mu_brake
    K_A_land = dens/((2*MLW)/S)*(-CD0_land)
    s_B = -(1/(2*g*K_A_land))*log((K_T_land+(K_A_land*V_TD**2))/K_T_land)
    
    s_total_land = s_A+s_F+s_FR+s_B
    landing_distances.append(s_total_land*1.66)
    if alt ==0:
        print "The approach distance is:",s_A, "m"
        print "The flare distance is:",s_F, "m"
        print "The free roll distance is:",s_FR, "m"
        print "The braking distance is:",s_B, "m"
        print "The total landing distance is:",s_total_land, "m"
        print "The landing distance including the factor to account for operational variances [1.66] is",s_total_land*1.66, "m"
    
plt.plot(altitude,takeoff_distances,label="Take-off performance")
plt.plot(altitude,landing_distances,label="Landing performance")
plt.grid(True)
plt.xlabel('Airport altitude [m]')
plt.ylabel('Take-off distance [m]')
plt.legend(loc=4)
plt.title('Take-off distance as a function of airport altitude')
#plt.text(500, 2400, r'Sea level take-off distance:1903 m') #make sure to change this value
plt.show()
#-----Second-segment climb


    
#------------Balanced field length
#V_failure = []
#dis_covered = []
#
#for failurespeed in range(1,100,1):
#    M_takeoff_failure = i/a
#    ratio_net_to_static = (1-(2*M_takeoff_failure*((1+lamda)/(3+2*lamda))))
#    K_T_failure = (ratio_net_to_static*thrust/MTOW)-mu_roll
#    K_A_failure = dens/((2*MTOW)/S)*(-CD_to+(mu_roll*CL_to))
#    
#    x_groundrun_failure = (1/(2*g*K_A))*log((K_T+(K_A*failurespeed**2))/K_T) #distance covered to failure speed
#    V_failure.append(failurespeed)
#    dis_covered.append(x_groundrun_failure)
#    
#speeds = np.arange(1,100,1)
#
#thrust2 = thrust*0.5

##-------------VERIFICATION GROUNDRUN------------------
#
##----- constants
#g = 9.80665
#MTOW = 230000. *g #68731
#mu_roll = 0.02
#mu_brake = 0.3
#alt = raw_input("Input the altitude of the airport in meters:")
#alt = eval(alt)
#dens = ISA(alt)[2]
#Temp = ISA(alt)[0]
#S = 376.4 #128. 
#thrust = 660970. #220000.
#oswald = 0.85
#gamma_climb = radians(3.)
#gamma_land =radians(3.)
#h_scr = 15.24 #screen height in m change to 15.24
#a = sqrt(1.4*287*Temp)
#M_takeoff = V_LOF/a
#CL_max_to = 1.75
#CL_to = 0.7
#CL_max_land = 2.5
#CD0_land = 0.055
#MLW = 184000.*9.80665
#n_land = 1.2
##------ ground roll
#V_min_to = sqrt((MTOW/S)*(2/dens)*(1/CL_max_to))
#V_LOF = V_min_to*1.1
#V_TRANS =1.15 *V_min_to
#V2 = V_min_to*1.2
##CD0_to = 0.04
#CD_to = 0.035 + 0.05*(CL_to**2)
##CD_to = CD0_to + (CL_to)**2/(pi*A*oswald)
##ratio_net_to_static = (1-(2*M_takeoff*((1+lamda)/(3+2*lamda)))) #from CADP p. 412 chapter 10, Jenkinson suggests using 0.864
#ratio_net_to_static = 0.864
#K_T = (ratio_net_to_static*thrust/MTOW)-mu_roll
#K_A = dens/((2*MTOW)/S)*(-CD_to+(mu_roll*CL_to))
#
#x_groundrun = (1/(2*g*K_A))*log((K_T+(K_A*V_LOF**2))/K_T)
#
#print "The groundrun distance is:", x_groundrun, "m"
##-------Transition to climb
#n = 1.2 #loadfactor climb 
#r = 7380/(g*(n-1)) #m
#
##------Final climb gradient
#CL_climb = CL_max_to/(1.2)**2
#CD_climb = 0.025 + 0.05*(CL_climb**2) #CD gear up, takeoff flaps
#D_climb = 0.5 * dens * (V2**2) * S * CD_climb
#climb_gradient = (0.803*thrust - D_climb)/(MTOW)
#x_transition = r * climb_gradient 
#print "The distance reached during transition is:", x_transition, "m"
#h_T = r*climb_gradient *(climb_gradient/2) #distance at end of transition
#x_screen = ((r+h_scr)**2 - r**2)**0.5
#print "The distance reached to reacht the screen height is:", x_screen, "m"
#x_total_takeoff = x_groundrun + x_screen
#
#print "The takeoff distance is", x_total_takeoff*1.15, "m"
#
#        
#Af = 2.50 #fan diameter
#CD_failedengine = 0.3*Af/S
#CD_trim = 0.05*CD_climb
#CD_secondsegmentclimb = CD_climb + CD_failedengine +CD_trim
#D_secondsegmentclimb = 0.5*dens * (V2)**2 *S * CD_secondsegmentclimb
#ratio_net_to_static_climb = 0.803
#climb_gradient_secondsegment_OEI = ((0.5*ratio_net_to_static_climb*thrust) - D_secondsegmentclimb)/(MTOW)
#
#if climb_gradient_secondsegment_OEI >= 0.024:
#    print "V - The climb gradient requirement for OEI during the second segment of climb is MET!"
#else:
#    print "X - The climb gradient requirement for OEI during the second segment of climb is NOT MET!"
#    
#print "The climb gradient in the second segment climb is:", climb_gradient_secondsegment_OEI, "m"
#V_min_land = sqrt((MLW/S)*(2/dens)*(1/CL_max_land))
#V_F = (1.15+1.3)*V_min_land/2
#V_TD = 1.15*V_min_land
#r_land = V_F**2/(9.80665*(n_land-1.))
#h_F = (r_land*gamma_land*gamma_land)/2.
#s_A = (h_scr-h_F)/tan(gamma_land) #approach distance
#s_F = r_land * gamma_land #flare distance
#s_FR = 2*V_TD  #free roll distance
#
#K_T_land = -mu_brake
#K_A_land = dens/((2*MLW)/S)*(-CD0_land)
#s_B = -(1/(2*g*K_A_land))*log((K_T_land+(K_A_land*V_TD**2))/K_T_land)
#
#s_total_land = s_A+s_F+s_FR+s_B
#print "The total landing distance is,", s_total_land, "m and", s_total_land*1.66, "m including the factor for operational variances"
##------------Balanced field length
##V_failure = []
##dis_covered = []
#
##for failurespeed in range(1,100,1):
##    M_takeoff_failure = (failurespeed/a)*0.707
##    ratio_net_to_static_f = (1-(2*M_takeoff_failure*((1+lamda)/(3+2*lamda))))
##    K_T_failure_1 = (ratio_net_to_static_f*thrust/MTOW)-mu_roll
##    K_A_failure_1 = dens/((2*MTOW)/S)*(-CD_to+(mu_roll*CL_to))
##    x_groundrun_failure_1 = (1/(2*g*K_A_failure))*log((K_T_failure+(K_A_failure*failurespeed**2))/K_T_failure) #distance covered to failure speed
##    
##    K_T_failure_2 = (ratio_net_to_static_f*(thrust/2)/MTOW)-mu_roll
##    K_A_failure_2 = dens/((2*MTOW)/S)*(-CD_to+(mu_roll*CL_to))
##    x_groundrun_failure_2 = (1/(2*g*K_A_failure_2))*log((K_T_failure_2+(K_A_failure_2*(V_LOF-((failurespeed)**2))/K_T_failure_2)))   
##    print x_groundrun_failure_2
##    x_covered_accelerate_go = x_groundrun_failure_1 + x_groundrun_failure_2     
##    V_failure.append(failurespeed)
##    dis_covered.append(x_covered_accelerate_go)
##
##plt.plot(V_failure,dis_covered)
##plt.show()