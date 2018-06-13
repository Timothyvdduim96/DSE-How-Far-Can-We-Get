# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:08:21 2018

@author: helua
"""

import numpy as np
from math import *
from parameters import ISA
import matplotlib.pyplot as plt

A = 14.75
g = 9.80665
<<<<<<< HEAD
thrust = 230000.
MTOW = 67834.*g#67834.2*g#68731. *g
=======
thrust = 213000.
MTOW = 67834.2*g#68731. *g
>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
S = 110.
oswald = 0.7276
CL_max_clean = 0.8
lamda = 14.
K = 1/(3.141*A*oswald)
rho_0 = 1.225
Vc_sealevel = []
Vc_5000 = []
Vc_10000 = []
Vc_15000 = []
Vc_20000 = []
Vc_25000 = []
Vc_30000 = []
Vc_35000 = []
Vc_39000 = []
R =287.
Vc_sealevel_uns = []
Vc_5000_uns = []
Vc_10000_uns = []
Vc_15000_uns = []
Vc_20000_uns = []
Vc_25000_uns = []
Vc_30000_uns = []
Vc_35000_uns = []
Vc_39000_uns = []
speeds_sealevel = []
speeds_5000 = []
speeds_10000= []
speeds_15000= []
speeds_20000= []
speeds_25000= []
speeds_30000= []
speeds_35000= []
speeds_39000= []
palist_0 = []
palist_5000 = []
palist_10000 = []
palist_15000 = []
palist_20000 = []
palist_25000 = []
palist_35000 = []
palist_30000 = []
palist_39000 = []
prlist_0 = []
prlist_5000 = []
prlist_10000 = []
prlist_15000 = []
prlist_20000 = []
prlist_25000 = []
prlist_30000 = []
prlist_35000 = []
prlist_39000 = []
gamma = 1.4
#h = 0.

CD0 = 0.01528
#V_min = sqrt((MTOW/S)*(2/dens)*(1/CL_max_clean))
#alt = [0,1524]

V_min0 = int(sqrt((MTOW/S)*(2/1.225)*(1/CL_max_clean)))
for V in range(V_min0,300,1):     
    P_alt = ISA(0)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(0)[0]
    dens = ISA(0)[2]
    a = sqrt(1.4*287.*Temp)
    M_c = V/a
<<<<<<< HEAD
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)  
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)   
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7  
    T_a = thrust*ratio 
=======
    V = sqrt(rho_0/dens)*V  
    
    # ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    # ratio = (P_alt/P_0) *sqrt(T_0/Temp)  
    # ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)   
    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
    T_a = thrust*ratio #* ratio_speed#*  ratio_net_to_static
>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
    #print T_a
    
    #print ratio  
    CL = MTOW/(0.5*dens*V**2*S)
    #print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D =  CD*0.5*dens*V**2*S
    #print D    
    #print CL/CD
    pr = D*V
    #print pr
    pa = T_a * V
    #print pa
    
    
    Vc = ((pa - pr)/MTOW)*196.58
    # if Vc <= 0:
    #     break
    palist_0.append(pa)
    prlist_0.append(pr)
    
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_sealevel_uns.append(Vc_uns)
    Vc_sealevel.append(Vc)
    speeds_sealevel.append(V)
<<<<<<< HEAD
    
=======


>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
V_min5000 = int(sqrt((MTOW/S)*(2/ISA(1524)[2])*(1/CL_max_clean)))
for V in range(V_min5000,300,1):     
    P_alt = ISA(1524)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(1524)[0]
    dens = ISA(1524)[2]
    a = sqrt(1.4*287*Temp)
    M_c = V/a
<<<<<<< HEAD
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
    
    
    
=======
    V = sqrt(rho_0/dens)*V 
>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
#    
    #T_a = dens*A_eng*V_eng*(Vj-V)
    T_a = thrust*ratio #*ratio_net_to_static
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
<<<<<<< HEAD
#    if Vc <= 0:
#        break
=======
    # if Vc <= 0:
    #     break
>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_5000_uns.append(Vc_uns)
    Vc_5000.append(Vc)
    speeds_5000.append(V)
'''
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
    
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
    
    
    
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
   
    T_a = thrust*ratio#*ratio_net_to_static
    #T_a = dens*A_eng*V_eng*(Vj-V)
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
#    if Vc <= 0:
#        break
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
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
    
    
    
    
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
     
    T_a = thrust*ratio#*ratio_net_to_static
    #T_a = dens*A_eng*V_eng*(Vj-V)
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
#    if Vc <= 0:
#        break
    palist_15000.append(pa)
    prlist_15000.append(pr)
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_15000_uns.append(Vc_uns)
    Vc_15000.append(Vc)
    speeds_15000.append(V)

V_min20000 = int(sqrt((MTOW/S)*(2/ISA(6096)[2])*(1/CL_max_clean)))
for V in range(V_min20000,300,1):     
    P_alt = ISA(6096 )[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(6096 )[0]
    dens = ISA(6096 )[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
    
    
    
    
    
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
   
    
    T_a = thrust*ratio#*ratio_net_to_static
    #print V    
    #T_a = dens*A_eng*V_eng*(Vj-V)    
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
#    if Vc <= 0:
#        break
    palist_20000.append(pa)
    prlist_20000.append(pr)
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_20000_uns.append(Vc_uns)
    Vc_20000.append(Vc)
    speeds_20000.append(V)
    
V_min25000 = int(sqrt((MTOW/S)*(2/ISA(7620)[2])*(1/CL_max_clean)))
for V in range(V_min25000,300,1):     
    P_alt = ISA(7620)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(7620)[0]
    dens = ISA(7620)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
   
   
   
   
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
    
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
#   
    T_a = thrust*ratio#*ratio_net_to_static
    #print V    
    #T_a = dens*A_eng*V_eng*(Vj-V)    
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
#    if Vc <= 0:
#        break
    palist_25000.append(pa)
    prlist_25000.append(pr)
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_25000_uns.append(Vc_uns)
    Vc_25000.append(Vc)
    speeds_25000.append(V)

#____nog aanpassen
V_min30000 = int(sqrt((MTOW/S)*(2/ISA(9144)[2])*(1/CL_max_clean)))
for V in range(V_min30000,300,1):     
    P_alt = ISA(9144 )[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(9144)[0]
    dens = ISA(9144)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
#   
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
    
    
    T_a = thrust*ratio#*ratio_net_to_static
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
#    if Vc <= 0:
#        break
    palist_30000.append(pa)
    prlist_30000.append(pr)
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_30000_uns.append(Vc_uns)
    Vc_30000.append(Vc)
    speeds_30000.append(V)

V_min35000 = int(sqrt((MTOW/S)*(2/ISA(10668)[2])*(1/CL_max_clean)))
for V in range(V_min35000,300,1):     
    P_alt = ISA(10668)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(10668)[0]
    dens = ISA(10668)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
   
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
    T_a = thrust*ratio#*ratio_net_to_static
    #print V    
    CL = MTOW/(0.5*dens*V**2*S)
    #print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D = (CD/CL)*MTOW#CD*0.5*dens*V**2*S
    #print CL/CD
    pr = D*V
    #print pr
    pa = T_a * V
    
    
    #palist.append(pa)
    #prlist.append(pr)
    Vc = ((pa - pr)/MTOW)*196.85
    print Vc
#    if Vc <= 0:
#        break
    palist_35000.append(pa)
    prlist_35000.append(pr)
    
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_35000_uns.append(Vc_uns)
    Vc_35000.append(Vc)
    speeds_35000.append(V)

V_min39000 = int(sqrt((MTOW/S)*(2/ISA(11887.2)[2])*(1/CL_max_clean)))
for V in range(V_min39000,300,1):     
    P_alt = ISA(11887.2)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(11887.2)[0]
    dens = ISA(11887.2)[2]
    a = sqrt(1.4*287*Temp)
    V = sqrt(rho_0/dens)*V      
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    #ratio = (P_alt/P_0) *sqrt(T_0/Temp)    
    #ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.48)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)       
#    A = (-0.4327*(P_alt/P_0)**2) + (1.3855*(P_alt/P_0))  + 0.0472   
#    Z = (0.9106*(P_alt/P_0)**3) - (1.7736*(P_alt/P_0)**2) + (1.8697*(P_alt/P_0))
#    X = (0.1377*(P_alt/P_0)**3) - (0.4374*(P_alt/P_0)**2) + (1.3003*(P_alt/P_0))
#    ratio = A - (((0.377*(1+lamda))/(sqrt((1+(0.82*lamda))*1.48)))*Z*M_c) + ((0.23+(0.19*sqrt(lamda)))*X*M_c**2)
    if M_c < 0.4: 
        K1 = 1.
        K2 = 0.
        K3 =-0.595
        K4 = -0.03
    else:
        K1 = 0.89
        K2 = -0.014
        K3 = -0.30
        K4 = 0.005
    sigma = dens/rho_0    
    ratio = (K1 + (K2*lamda) +(K3+(K4*lamda))*M_c)*sigma**0.7 
    T_a = thrust*ratio#*ratio_net_to_static
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
#    if Vc <= 0:
#        break
    palist_39000.append(pa)
    prlist_39000.append(pr)
    Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    Vc_39000_uns.append(Vc_uns)
    Vc_39000.append(Vc)
    speeds_39000.append(V)


#power available/required
plt.subplot(2,2,1)
<<<<<<< HEAD
plt.plot(speeds_sealevel,palist_0,label="Pa Sea level")
plt.plot(speeds_5000,palist_5000, label="Pa 5000 ft")
plt.plot(speeds_10000,palist_10000, label="Pa 10000 ft") 
plt.plot(speeds_15000,palist_15000, label="Pa 15000 ft")
plt.plot(speeds_20000,palist_20000, label="Pa 15000 ft")
plt.plot(speeds_25000,palist_25000, label="Pa 15000 ft")
plt.plot(speeds_sealevel,prlist_0, label="Pr Sea level") #plt.plot(speeds_sealevel,prlist_0,label="Pr Sea level")
plt.plot(speeds_5000,prlist_5000, label="Pr 5000 ft")
plt.plot(speeds_10000,prlist_10000, label="Pr 10000 ft")
plt.plot(speeds_15000,prlist_15000, label="Pr 15000 ft")
plt.plot(speeds_20000,prlist_20000, label="Pr 20000 ft")
plt.plot(speeds_25000,prlist_25000, label="Pr 25000 ft")
#plt.plot(speeds_30000,prlist_30000, label="Pr 30000 ft")
#plt.plot(speeds_35000,prlist_35000, label="Pr 35000 ft")
=======
# plt.plot(speeds_sealevel,palist_0,label="Pa Sea level")
# plt.plot(speeds_5000,palist_5000, label="Pa 5000 ft")
#plt.plot(speeds_10000,palist_10000, label="Pa 10000 ft") 
#plt.plot(speeds_15000,palist_15000, label="Pa 15000 ft")
#plt.plot(speeds_35000,prlist_35000, label="Pr 39000 ft") 
plt.plot(speeds_sealevel,prlist_0,label="Pr Sea level")
plt.plot(speeds_5000,prlist_5000, label="Pr 5000 ft")
#plt.plot(speeds_10000,prlist_10000, label="Pr 10000 ft")
#plt.plot(speeds_15000,prlist_15000, label="Pr 15000 ft")
#plt.plot(speeds_35000,prlist_35000, label="Pr 39000 ft")
>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
plt.xlabel('Velocity [m/s]')
plt.ylabel('Power available/required')
plt.legend(loc=4)
plt.title('Power available/required vs speed')
plt.grid(True)

#Steady performance
plt.subplot(2,2,2)
plt.axis((0,400,0,6000))
plt.plot(speeds_sealevel,Vc_sealevel,label="Sea level")
plt.plot(speeds_5000,Vc_5000,label="5000 ft")
<<<<<<< HEAD
plt.plot(speeds_10000,Vc_10000, label="10000 ft")
plt.plot(speeds_15000,Vc_15000, label="15000 ft")
plt.plot(speeds_20000,Vc_20000, label="20000 ft")
plt.plot(speeds_25000,Vc_25000, label="25000 ft")
=======
#plt.plot(speeds_10000,Vc_10000, label="10000 ft")
#plt.plot(speeds_15000,Vc_15000, label="15000 ft")
#plt.plot(speeds_20000,Vc_20000, label="20000 ft")
#plt.plot(speeds_25000,Vc_25000, label="25000 ft")
>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
#plt.plot(speeds_30000,Vc_30000, label="30000 ft")
#plt.plot(speeds_35000,Vc_35000, label="35000 ft")
#plt.plot(speeds_39000,Vc_39000, label="39000 ft")
plt.xlabel('Velocity [m/s]')
plt.ylabel('Rate of climb [ft/min]')
plt.legend(loc=4)
plt.title('Steady Rate of climb')
plt.grid(True)

#Steady performance
plt.subplot(2,2,3)
plt.axis((0,400,0,6000))
plt.plot(speeds_sealevel,Vc_sealevel_uns,label="Sea level")
plt.plot(speeds_5000,Vc_5000_uns,label="5000 ft")
<<<<<<< HEAD
plt.plot(speeds_10000,Vc_10000_uns, label="10000 ft")
plt.plot(speeds_15000,Vc_15000_uns, label="15000 ft")
plt.plot(speeds_20000,Vc_20000_uns, label="20000 ft")
plt.plot(speeds_25000,Vc_25000_uns, label="25000 ft")
=======
#plt.plot(speeds_10000,Vc_10000_uns, label="10000 ft")
#plt.plot(speeds_15000,Vc_15000_uns, label="15000 ft")
#plt.plot(speeds_20000,Vc_20000_uns, label="20000 ft")
#plt.plot(speeds_25000,Vc_25000_uns, label="25000 ft")
>>>>>>> 8356a77972c6365182e16c9a59c5f703cf55bdf7
#plt.plot(speeds_30000,Vc_30000_uns, label="30000 ft")
#plt.plot(speeds_35000,Vc_35000_uns, label="35000 ft")
#plt.plot(speeds_39000,Vc_39000_uns, label="39000 ft")
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
'''

A = 12.
g = 9.80665
thrust = 213000.
MTOW = 150000.
S = 70.
oswald = 0.76
CL_max_clean = 1.5
lamda = 14.
K = 1/(3.141*A*oswald)
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

CD0 = 0.013
#V_min = sqrt((MTOW/S)*(2/dens)*(1/CL_max_clean))
#alt = [0,1524]

V_min0 = int(sqrt((MTOW/S)*(2/1.225)*(1/CL_max_clean)))
for V in range(V_min0,180,1):     
    P_alt = ISA(0)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(0)[0]
    dens = ISA(0)[2]
    a = sqrt(1.4*287*Temp)
   # V = sqrt(rho_0/dens)*V  
    M_c = V/a
    #ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    ratio = (P_alt/P_0) *sqrt(T_0/Temp)  
    ratio_speed = 1- ((0.377*(1+lamda))/sqrt((1+(0.82*lamda))*1.5)*M_c) + ((0.23+(0.19*sqrt(lamda)))*M_c**2)   
    T_a = thrust*ratio*ratio_speed #*  ratio_net_to_static
    #print ratio  
    CL = MTOW/(0.5*dens*V**2*S)
    #print CL
    CD = CD0 + (CL**2/(pi*A*oswald))
    D =  (CD/CL)*MTOW#CD*0.5*dens*V**2*S
    #print D    
    #print CL/CD
    pr = D*V
    V = V *3.6
    #print pr
    #pa = T_a * V
    #print pa
    
    #palist_0.append(pa)
    prlist_0.append(pr/1000)
    # Vc = ((pa - pr)/MTOW)*196.58
    # if Vc <= 0:
    #     break
    
    # Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    # Vc_sealevel_uns.append(Vc_uns)
    # Vc_sealevel.append(Vc)
    speeds_sealevel.append(V)



V_min5000 = int(sqrt((MTOW/S)*(2/ISA(3000)[2])*(1/CL_max_clean)))
for V in range(V_min5000,180,1):     
    P_alt = ISA(3000)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(3000)[0]
    dens = ISA(3000)[2]
    a = sqrt(1.4*287*Temp)
    #V = sqrt(rho_0/dens)*V  
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
    V = V*3.6
    #print pr
    #pa = T_a * V
    #print pa
    
    #palist_5000.append(pa)
    prlist_5000.append(pr/1000)
    # Vc = ((pa - pr)/MTOW)*196.58
    # if Vc <= 0:
    #     break
    # Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    # Vc_5000_uns.append(Vc_uns)
    # Vc_5000.append(Vc)
    speeds_5000.append(V)

V_min10000 = int(sqrt((MTOW/S)*(2/ISA(6000)[2])*(1/CL_max_clean)))
for V in range(V_min10000,180,1):     
    P_alt = ISA(6000)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(6000)[0]
    dens = ISA(6000)[2]
    a = sqrt(1.4*287*Temp)
    #V = sqrt(rho_0/dens)*V      
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
    V = V*3.6
    #print pr
    #pa = T_a * V
    #print pa
    
    #palist_10000.append(pa)
    prlist_10000.append(pr/1000)
    #palist.append(pa)
    #prlist.append(pr)
    #Vc = ((pa - pr)/MTOW)*196.85
    # if Vc <= 0:
    #     break
    # Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    # Vc_10000_uns.append(Vc_uns)
    # Vc_10000.append(Vc)
    speeds_10000.append(V)


V_min15000 = int(sqrt((MTOW/S)*(2/ISA(9000)[2])*(1/CL_max_clean)))
for V in range(V_min15000,180,1):     
    P_alt = ISA(9000)[1]
    P_0 = ISA(0)[1]
    T_0 = ISA(0)[0]
    Temp = ISA(9000)[0]
    dens = ISA(9000)[2]
    a = sqrt(1.4*287*Temp)
    #V = sqrt(rho_0/dens)*V  
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
    V = V*3.6
    #print pr
    #pa = T_a * V
    #print pa
    
    #palist_15000.append(pa)
    prlist_15000.append(pr/1000)
    # Vc = ((pa - pr)/MTOW)*196.58
    # if Vc <= 0:
    #     break
    # Vc_uns = ((1+((M_c**2*gamma/2)*(((R/g)*-0.0065)+1)))**-1)*Vc
    # Vc_5000_uns.append(Vc_uns)
    # Vc_5000.append(Vc)
    speeds_15000.append(V)


plt.plot(speeds_sealevel,prlist_0, label="0 m")
plt.plot(speeds_5000,prlist_5000, label="3000 m")
plt.plot(speeds_10000,prlist_10000, label="6000 m")
plt.plot(speeds_15000,prlist_15000, label="9000 m")
plt.xlabel('Velocity [km/h]')
plt.ylabel('Power required [kW]')
plt.legend(loc=4)
plt.axis((0,600,0,2000))
plt.title('Power required vs speed')
plt.show()



#power available/required
plt.subplot(2,2,1)
plt.plot(speeds_sealevel,palist_0,label="Pa Sea level")
plt.plot(speeds_5000,palist_5000, label="Pa 5000 ft")
#plt.plot(speeds_10000,palist_10000, label="Pa 10000 ft") 
#plt.plot(speeds_15000,palist_15000, label="Pa 15000 ft") 
plt.plot(speeds_sealevel,prlist_0,label="Pr Sea level")
plt.plot(speeds_5000,prlist_5000, label="Pr 5000 ft")
#plt.plot(speeds_10000,prlist_10000, label="Pr 10000 ft")
#plt.plot(speeds_15000,prlist_15000, label="Pr 15000 ft")
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
'''