# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 12:15:16 2018

@author: helua
"""

import numpy as np
from math import *
import matplotlib.pyplot as plt
from parameters import rho_0,g,A,ISA
from TWWS import C_L_maxto,C_Lcr,C_Lland,C_D_0,thrust,S
from liftdrag import C_L_cr
h = raw_input("Enter take-off altitude in m")
h = eval(h)
T0 = ISA(h)[0]
rho = ISA(h)[2]
a0 = (1.4*287*T0)**0.5

W = 72564.*g
lamda = 14.
mu_roll = 0.02 #roll friction coefficient
gamma_to = radians(3) #takeoff climb
h_to = 15.24 #screen height
F_to = thrust * 1000 #takeoff static thrust in kN
V_to = sqrt(2*(W/S)/(rho*C_L_maxto))
M_to = V_to/a0

C_D0 = 0.07
CD_takeoff = C_D0 + (C_L_maxto**2/(pi*A*e))

D_takeoff = CD_takeoff * 0.5 * rho * (V_to)**2 * S
L_takeoff = C_L_maxto * 0.5 * rho * (V_to)**2 * S
dragratio_takeoff = D_takeoff/L_takeoff
Favg_to = F_to*(1-(M_to*((1+lamda)/(3+(2*lamda))))) #average net thrust
ratio = Favg_to/W
xg = -(V_to**2/(2*g))*(1/((dragratio_takeoff)-mu_roll))*log((ratio-dragratio_takeoff)/(ratio-mu_roll))
xair = (((1/(20*g))*(V_to)**2)+h_to)/(sin(gamma_to))
x_total_to = xg + xair

print "The groundrun distance is:",xg, "m"
print "The distance in air is:", xair, "m"
print "The total takeoff distance is:", x_total_to, "m"

Vs = sqrt(2*W/S/(rho*C_Lland))
V_ap = 1.3*Vs
Ve = 1.2*Vs #speed of aircraft at end of air run
gamma_land = 3

C_D0 = 0.08
CD_land = C_D0 + (C_Lland**2/(pi*A*e))

D_land = CD_land * 0.5 * rho * (V_ap)**2 * S
L_land = C_Lland * 0.5 * rho * (V_ap)**2 * S
dragratio_land = D_land/L_land

xair_land = (1/(2*g))*((Ve**2-V_ap**2)/(-dragratio_land+gamma_land))

print "--------------------Landing performance--------------------"
print "The distance in air during landing is:", xair_land, "m" 



