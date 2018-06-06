# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:50:15 2018

@author: helua
"""
#Tool calculating take-off/landing performance

import numpy as np
from math import *
import matplotlib.pyplot as plt
from parameters import rho_0,g,A
from TWWS import C_L_maxto, thrust, C_D_0,C_Lcr
#from liftdrag import C_L_cr

print "-------------Take-off performance-----------------"
print "Choose the thrust setting from 0 to 1"
thrust_setting = float(raw_input("What is the thrust setting"))
#constants
MTOW = 72564.*g #Maximum take-off weight in kg
S = 128. #wing surface area in m^2
#rho_0= 1.225 #sea level density kg/m^3
#C_L_max = 2.3 #Maximum CL
#T = 170000. #Thrust in kN
e = 0.85
gamma_climb = radians(3) #degrees
hscr = 15. #screen height in m
#Intermediate calculations
V_min = sqrt((MTOW/S)*(2/rho_0)*(1/C_L_maxto)) #Minimum speed in m/s
V_LOF = 1.05*V_min #Lift of speed in m/s
V = V_LOF/sqrt(2) #average speed
CD = C_D_0 + (C_Lcr**2/(pi*A*e))
D = CD * 0.5 * rho_0 * V**2 * S
L = C_Lcr * 0.5 * rho_0 * V**2 * S
#L = CL * 0.5 * rho_0 * V**2 * S
Dg = 0.02*(MTOW-L) #GROUND drag with a friction coefficient of 0.02
a_bar = (g/MTOW)*((thrust*1000*thrust_setting)-D-Dg) #average acceleration during ground run in m/s^2

#Output
s = (V_LOF**2)/(2*a_bar) #ground run distance in m
x_trans = (V_LOF**2/(0.15*g)) * sin(gamma_climb)
x_climb = (hscr - ((1-cos(gamma_climb)) * (V_LOF**2/(0.15*g))))/tan(gamma_climb)
x_total_airborne = x_trans + x_climb

x_total = s + x_total_airborne

print
print "The lift of speed is:", V_LOF, "m/s"
print "The ground run distance is:", s, "m"
print "The airborne distance is:", x_total_airborne, "m"
print "The total take-off distance is:", x_total, "m"

