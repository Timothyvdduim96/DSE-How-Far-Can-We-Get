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
thrust = 220000.
MTOW = 68731. *g
S = 128.
oswald = 0.85
CL_max_clean = 0.8
lamda = 14.
K = 1/pi*A*oswald

Vc_sealevel = []
speeds_sealevel = []
palist = []
prlist = []
h = 0.
Temp = ISA(h)[0]
dens = ISA(h)[2]
CD0 = 0.0165
V_min = sqrt((MTOW/S)*(2/dens)*(1/CL_max_clean))

    
for V in range(104,300,1):   
    a = sqrt(1.4*287*Temp)
    M_c = V/a
    ratio_net_to_static = (1-(2*M_c*((1+lamda)/(3+2*lamda))))
    T_a = thrust*ratio_net_to_static    
    #print V    
    CL = MTOW/(0.5*dens*V**2*S)
    print CL
    CD = CD0 + K*(CL**2)
    D = CD*0.5*dens*V**2*S
    
    pr = D*V
    pa = T_a * V
    
    palist.append(pa)
    prlist.append(pr)
    Vc = (pa - pr)/MTOW
    Vc_sealevel.append(Vc)
    speeds_sealevel.append(V)
    
#plt.plot(speeds_sealevel,Vc_sealevel,label="Sea level")
plt.plot(speeds_sealevel,palist)
#plt.plot(speeds_sealevel,prlist)
plt.grid(True)
plt.xlabel('Velocity [m/s]')
plt.ylabel('Rate of climb [ft/min]')
plt.legend(loc=4)
plt.title('Rate of climb')
#plt.text(500, 2400, r'Sea level take-off distance:1706 m') #make sure to change this value
plt.show()

#------------
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

