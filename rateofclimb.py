# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:08:21 2018

@author: helua
"""

import numpy as np
from math import *
from parameters import ISA
import matplotlib.pyplot as plt

A = 14.
g = 9.80665
thrust = 213000.
MTOW = 67834.2*g#68731. *g
S = 110.
oswald = 0.85
CL_max_clean = 0.8
lamda = 14.
K = 1/3.141*A*oswald
rho_0 = 1.225
Vc_sealevel = []
Vc_5000 = []
Vc_10000 = []
Vc_15000 = []
Vc_20000 = []
R =287
Vc_sealevel_uns = []
Vc_5000_uns = []
Vc_10000_uns = []
Vc_15000_uns = []
Vc_20000_uns = []
speeds_sealevel = []
speeds_5000 = []
speeds_10000= []
speeds_15000= []
speeds_20000= []
palist_0 = []
palist_5000 = []
palist_10000 = []
palist_15000 = []
palist_20000 = []
prlist_0 = []
prlist_5000 = []
prlist_10000 = []
prlist_15000 = []
prlist_20000 = []
gamma = 1.4
#h = 0.

CD0 = 0.0165
#V_min = sqrt((MTOW/S)*(2/dens)*(1/CL_max_clean))
#alt = [0,1524]

V_min0 = int(sqrt((MTOW/S)*(2/1.225)*(1/CL_max_clean)))
for V in range(V_min0,300,1):     
    P_alt = ISA(0)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(0)[0]
    dens = ISA(0)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V  
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    ratio = (P_alt/P_0) *sqrt(T_0/Temp)  
    ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.5)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)   
    T_a = thrust*ratio*ratio_speed #*  ratio_net_to_static
    #print ratio  
    CL = MTOW/(0.5*dens*V**2*S)
    print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D =  (CD/CL)*MTOW#CD*0.5*dens*V**2*S
    #print D    
    #print CL/CD
    pr = D*V
    #print pr
    pa = T_a * V
    #print pa
    
    palist_0.append(pa)
    prlist_0.append(pr)
    Vc = ((pa - pr)/MTOW)*196.58
    if Vc <= 0:
        break
    
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_sealevel_uns.append(Vc_uns)
    Vc_sealevel.append(Vc)
    speeds_sealevel.append(V)

V_min5000 = int(sqrt((MTOW/S)*(2/ISA(1524)[2])*(1/CL_max_clean)))
for V in range(V_min5000,300,1):     
    P_alt = ISA(1524)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(1524)[0]
    dens = ISA(1524)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V    
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.5)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
    T_a = thrust*ratio*ratio_speed #*ratio_net_to_static
    #print ratio 
    #print V    
    CL = (MTOW/(0.5*dens*V**2*S))
    #print CL
    #print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D = (CD/CL)*MTOW#CD*0.5*dens*V**2*S
    #print D
    #print CL/CD
    pr = D*V
    #print pr
    pa = T_a * V
    #print pa
    
    palist_5000.append(pa)
    prlist_5000.append(pr)
    Vc = ((pa - pr)/MTOW)*196.58
    if Vc <= 0:
        break
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_5000_uns.append(Vc_uns)
    Vc_5000.append(Vc)
    speeds_5000.append(V)

V_min10000 = int(sqrt((MTOW/S)*(2/ISA(3048)[2])*(1/CL_max_clean)))
for V in range(V_min10000,300,1):     
    P_alt = ISA(3048)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(3048)[0]
    dens = ISA(3048)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.5)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
    T_a = thrust*ratio*ratio_speed#*ratio_net_to_static
    #print V    
    CL = MTOW/(0.5*dens*V**2*S)
    #print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D = (CD/CL)*MTOW#CD*0.5*dens*V**2*S
    #print CL/CD
    pr = D*V
    #print pr
    pa = T_a * V
    #print pa
    
    palist_10000.append(pa)
    prlist_10000.append(pr)
    #palist.append(pa)
    #prlist.append(pr)
    Vc = ((pa - pr)/MTOW)*196.85
    if Vc <= 0:
        break
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_10000_uns.append(Vc_uns)
    Vc_10000.append(Vc)
    speeds_10000.append(V)
    

V_min15000 = int(sqrt((MTOW/S)*(2/ISA(4572)[2])*(1/CL_max_clean)))
for V in range(V_min15000,300,1):     
    P_alt = ISA(4572)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(4572)[0]
    dens = ISA(4572)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.5)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
    T_a = thrust*ratio*ratio_speed#*ratio_net_to_static
    #print V    
    CL = MTOW/(0.5*dens*V**2*S)
    #print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D = (CD/CL)*MTOW#CD*0.5*dens*V**2*S
    #print CL/CD
    pr = D*V
    #print pr
    pa = T_a * V
    #print pa
    
    
    #palist.append(pa)
    #prlist.append(pr)
    Vc = ((pa - pr)/MTOW)*196.85
    if Vc <= 0:
        break
    palist_15000.append(pa)
    prlist_15000.append(pr)
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_15000_uns.append(Vc_uns)
    Vc_15000.append(Vc)
    speeds_15000.append(V)

V_min20000 = int(sqrt((MTOW/S)*(2/ISA(6096 )[2])*(1/CL_max_clean)))
for V in range(V_min20000,300,1):     
    P_alt = ISA(6096 )[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(6096 )[0]
    dens = ISA(6096 )[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.5)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
    T_a = thrust*ratio*ratio_speed#*ratio_net_to_static
    #print V    
    CL = MTOW/(0.5*dens*V**2*S)
    #print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D = (CD/CL)*MTOW#CD*0.5*dens*V**2*S
    #print CL/CD
    pr = D*V
    #print pr
    pa = T_a * V
    #print pa
    
    
    #palist.append(pa)
    #prlist.append(pr)
    Vc = ((pa - pr)/MTOW)*196.85
    if Vc <= 0:
        break
    palist_20000.append(pa)
    prlist_20000.append(pr)
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_20000_uns.append(Vc_uns)
    Vc_20000.append(Vc)
    speeds_20000.append(V)

#power available/required
plt.subplot(2,2,1)
plt.plot(speeds_sealevel,palist_0,label="Pa Sea level")
plt.plot(speeds_5000,palist_5000, label="Pa 5000 ft")
plt.plot(speeds_10000,palist_10000, label="Pa 10000 ft") 
plt.plot(speeds_15000,palist_15000, label="Pa 15000 ft") 
plt.plot(speeds_sealevel,prlist_0,label="Pr Sea level")
plt.plot(speeds_5000,prlist_5000, label="Pr 5000 ft")
plt.plot(speeds_10000,prlist_10000, label="Pr 10000 ft")
plt.plot(speeds_15000,prlist_15000, label="Pr 15000 ft")
plt.xlabel('Velocity [m/s]')
plt.ylabel('Power available/required')
plt.legend(loc=4)
plt.title('Power available/required vs speed')
plt.grid(True)

#Steady performance
plt.subplot(2,2,2)
plt.plot(speeds_sealevel,Vc_sealevel,label="Sea level")
plt.plot(speeds_5000,Vc_5000,label="5000 ft")
plt.plot(speeds_10000,Vc_10000, label="10000 ft")
plt.plot(speeds_15000,Vc_15000, label="15000 ft")
plt.plot(speeds_20000,Vc_20000, label="15000 ft")
plt.xlabel('Velocity [m/s]')
plt.ylabel('Rate of climb [ft/min]')
plt.legend(loc=4)
plt.title('Steady Rate of climb')
plt.grid(True)

#Steady performance
plt.subplot(2,2,3)
plt.plot(speeds_sealevel,Vc_sealevel_uns,label="Sea level")
plt.plot(speeds_5000,Vc_5000_uns,label="5000 ft")
plt.plot(speeds_10000,Vc_10000_uns, label="10000 ft")
plt.plot(speeds_15000,Vc_15000_uns, label="15000 ft")
plt.plot(speeds_20000,Vc_20000_uns, label="15000 ft")
plt.xlabel('Velocity [m/s]')
plt.ylabel('Rate of climb [ft/min]')
plt.legend(loc=4)
plt.title('Unsteady Rate of climb')
plt.grid(True)

#plt.plot(speeds_sealevel,Vc_sealevel_uns,label="Sea level - Unsteady")

#plt.plot(speeds_5000,Vc_5000, label="5000 ft")
#plt.plot(speeds_10000,Vc_10000, label="10000 ft")
#plt.plot(speeds_sealevel,palist)
#plt.plot(speeds_sealevel,prlist)
#plt.grid(True)
#plt.xlabel('Velocity [m/s]')
#plt.ylabel('Rate of climb [ft/min]')
#plt.legend(loc=4)
#plt.title('Rate of climb')
#plt.text(500, 2400, r'Sea level take-off distance:1706 m') #make sure to change this value
plt.show()

#------------
#
#for V in range(104,300,1):
#    a = sqrt(1.4*287*Temp)
#    M_c = V/a
#    ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
#    T_a = thrust*ratio_net_to_static    
#    
#    A = K*MTOW**2/(0.5*dens*V**2*S)
#    B = -MTOW
#    C = T_a-(0.5*dens*(V**2)*S*CD0)-((2*K*MTOW**2)/(dens*V**2*S))
#    D = (B**2) - (4*A*C)
#    sol1 = (-B-sqrt(D))/(2*A)
#    sol2 = (-B+sqrt(D))/(2*A)
#    sol = min(sol1,sol2)
#    
#    gamma = asin(sol)
#    Vc = V*sin(gamma)
#    Vc_sealevel.append(Vc)
#    speeds_sealevel.append(V)
#    
#plt.plot(speeds_sealevel,Vc_sealevel,label="Sea level")
#plt.grid(True)
#plt.xlabel('Velocity [m/s]')
#plt.ylabel('Rate of climb [ft/min]')
#plt.legend(loc=4)
#plt.title('Rate of climb')
##plt.text(500, 2400, r'Sea level take-off distance:1706 m') #make sure to change this value
#plt.show()

#-----VERIFICATION

#
##A = 14.
#g = 9.80665
#thrust = 907.*g
#MTOW = 4535.92*g
#S = 18.58
#oswald = 0.85
#CL_max_clean = 0.8
#lamda = 14.
#K = 1/3.141*A*oswald
#rho_0 = 1.225
#Vc_sealevel = []
#Vc_5000 = []
#Vc_10000 = []
#R =287
#Vc_sealevel_uns = []
#Vc_5000_uns = []
#Vc_10000_uns = []
#speeds_sealevel = []
#speeds_5000 = []
#speeds_10000= []
#palist_0 = []
#palist_5000 = []
#prlist_0 = []
#prlist_5000 = []
#gamma = 1.4
##h = 0.
#
##CD0 = 0.0165
#V_min = sqrt((MTOW/S)*(2/dens)*(1/CL_max_clean))
##alt = [0,1524]
#
##V_min0 = int(sqrt((MTOW/S)*(2/1.225)*(1/CL_max_clean)))   
#P_alt = ISA(0)[1]
#P_0 = ISA(0)[1]
#T_0 = ISA(0)[0]
#Temp = ISA(0)[0]
#dens = ISA(0)[2]
#a = sqrt(1.4*287*Temp)
#M_c = V/a
#V = 118.08
##ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
##ratio = (P_alt/P_0) *sqrt(T_0/Temp)  
#T_a = thrust #*  ratio_net_to_static
##print ratio  
#CL = 0.28
##print CL
#CD = 0.0239
#D =  (CD/CL)*MTOW#CD*0.5*dens*V**2*S
##print D    
##print CL/CD
#pr = D*V
##print pr
#pa = T_a * V
##print pa
#
#Vc = ((pa - pr)/MTOW)
#print Vc
##Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
##Vc_sealevel_uns.append(Vc_uns)
##Vc_sealevel.append(Vc)
##speeds_sealevel.append(V)
##
##V_min5000 = int(sqrt((MTOW/S)*(2/ISA(1524)[2])*(1/CL_max_clean)))
##for V in range(V_min5000,300,1):     
##    P_alt = ISA(1524)[1]
##    P_0 = ISA(0)[1]
##    T_0 = ISA(0)[0]
##    Temp = ISA(1524)[0]
##    dens = ISA(1524)[2]
##    a = sqrt(1.4*287*Temp)
##    V = sqrt(rho_0/dens)*V    
##    M_c = V/a
##    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
##    ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
##    T_a = thrust*ratio #*ratio_net_to_static
##    #print ratio 
##    #print V    
##    CL = MTOW/(0.5*dens*V**2*S)
##    #print CL
##    CD = CD0 + (CL**2/(pi*A*oswald))
##    D = (CD/CL)*MTOW#CD*0.5*dens*V**2*S
##    #print D
##    #print CL/CD
##    pr = D*V
##    #print pr
##    pa = T_a * V
##    #print pa
##    
##    palist_5000.append(pa)
##    prlist_5000.append(pr)
##    Vc = ((pa - pr)/MTOW)*196.58
##    if Vc <= 0:
##        break
##    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
##    Vc_5000_uns.append(Vc_uns)
##    Vc_5000.append(Vc)
##    speeds_5000.append(V)
##
##V_min10000 = int(sqrt((MTOW/S)*(2/ISA(3048)[2])*(1/CL_max_clean)))
##for V in range(V_min10000,300,1):     
##    P_alt = ISA(3048)[1]
##    P_0 = ISA(0)[1]
##    T_0 = ISA(0)[0]
##    Temp = ISA(3048)[0]
##    dens = ISA(3048)[2]
##    a = sqrt(1.4*287*Temp)
##    V = sqrt(rho_0/dens)*V      
##    M_c = V/a
##    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
##    ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
##    T_a = thrust*ratio#*ratio_net_to_static
##    #print V    
##    CL = MTOW/(0.5*dens*V**2*S)
##    #print CL
##    CD = CD0 + (CL**2/(pi*A*oswald))
##    D = (CD/CL)*MTOW#CD*0.5*dens*V**2*S
##    #print CL/CD
##    pr = D*V
##    #print pr
##    pa = T_a * V
##    #print pa
##    
##    #palist.append(pa)
##    #prlist.append(pr)
##    Vc = ((pa - pr)/MTOW)*196.85
##    if Vc <= 0:
##        break
##
##    Vc_10000.append(Vc)
##    speeds_10000.append(V)
#
##plt.plot(speeds_sealevel,palist_0,label="Sea level")
##plt.plot(speeds_5000,palist_5000, label="5000 ft")    
#
#
##plt.plot(speeds_sealevel,prlist_0,label="Sea level")
##plt.plot(speeds_5000,prlist_5000, label="5000 ft")
#
#
#plt.plot(speeds_5000,Vc_5000,label="Sea level")
#plt.plot(speeds_5000,Vc_5000_uns,label="Sea level - Unsteady")
#
##plt.plot(speeds_5000,Vc_5000, label="5000 ft")
##plt.plot(speeds_10000,Vc_10000, label="10000 ft")
##plt.plot(speeds_sealevel,palist)
##plt.plot(speeds_sealevel,prlist)
#plt.grid(True)
#plt.xlabel('Velocity [m/s]')
#plt.ylabel('Rate of climb [ft/min]')
#plt.legend(loc=4)
#plt.title('Rate of climb')
##plt.text(500, 2400, r'Sea level take-off distance:1706 m') #make sure to change this value
#plt.show()