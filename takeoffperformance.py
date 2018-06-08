# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 11:50:15 2018

@author: helua
"""
#Tool calculating take-off/landing performance

import numpy as np
from math import *
import matplotlib.pyplot as plt
from parameters import g
#from TWWS import C_L_maxto,C_Lcr,C_Lland,C_D_0,thrust
#from liftdrag import C_L_cr

print "-------------Take-off performance-----------------"
#print "Choose the thrust setting from 0 to 1"
#thrust_setting = float(raw_input("What is the thrust setting"))


#------------------constants-------------
rho_0 = 1.225
MTOW = 68731.*g #Maximum take-off weight in kg
#MTOW = 60000.
#A = 15.91**2/30
S = 128. #wing surface area in m^2
#S = 30.
#rho_0= 1.225 #sea level density kg/m^3
#C_L_max = 2.3 #Maximum CL
#T = 170000. #Thrust in kN
A = 14.
e = 0.85
gamma_climb = radians(3) #degrees
hscr = 15.24 #screen height in m
C_L_maxto = (2.01)/(1.1**2) #CL max takeoff
C_Lcr = 0.87 #CL max cruise
C_Lland = 2.47  #CL max landing
C_L_cr = 0.6167
C_D_0 = 0.07 #CDO
thrust = 220
#------------------------Intermediate calculations------------------
V_min = sqrt((MTOW/S)*(2/rho_0)*(1/C_L_maxto)) #Minimum speed in m/s, use max CL during take-off
#V_min = ((MTOW/S)*(2/rho_0)*(1/1.3))**0.5
V_LOF = 1.1*V_min #Lift of speed in m/s
V = V_LOF/sqrt(2) #average speed
CD = C_D_0 + (C_L_maxto**2/(pi*A*e)) #use max clean?, Which value for CL, because drag polar only accurate up to a certain CL
#CD = 0.08 + (0.6**2/(pi*A*e))
D = CD * 0.5 * rho_0 * V**2 * S
L = C_L_maxto * 0.5 * rho_0 * V**2 * S
#L = 0.6 * 0.5 * rho_0 * V**2 * S

Dg = 0.02*(MTOW-L) #GROUND drag with a friction coefficient of 0.02
a_bar = (g/MTOW)*((thrust*1000)-D-Dg) #average acceleration during ground run in m/s^2

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

#t = 0.
#time = []
#distance = []
#d0 = 0.
#dt = 1.
#velocity = 0.

#for i in range(0,1000):
#    velocity = a_bar*dt + velocity   
#    d0 = d0 + velocity*dt
#    distance.append(d0)
#    t = t + dt
#    time.append(t)
#    if distance >= s:
#        print t
#        break

#plt.plot(time,distance)
#plt.show()
    

print "-------------Landing performance"
MLW = (68731.-6385)*g
V_min_land = sqrt((MLW/S)*(2/rho_0)*(1/C_Lland))
V_ap = 1.3*V_min_land
gamma_approach = radians(3)
L_land = (C_Lcr+0.2)*(0.5)*rho_0*(V_ap/sqrt(2))**2*S #Lift coefficient in ground run attitude, which cl to use?

CD0_land = 0.07
CD_land = CD0_land + ((C_Lcr+0.2)**2/(pi*A*e))
D_land = CD_land*(0.5)*rho_0*(V_ap/sqrt(2))**2*S #
R = V_ap**2/(g*0.1)
#R = (1.3**2 *(((MTOW/S)*(2/rho_0)*(1/C_Lland))/(0.10*g)))
x_land_airborne= R*sin(gamma_approach) + (hscr-(1-cos(gamma_approach))*R)/tan(gamma_approach) #The airspeed is assumed constant during this phase
x_tr=2*V_ap
Trev = thrust*1000*0.
Dg_land = 0.4*(MLW-L_land)
#x_brake=((MTOW**2)/(2*g*S))*(2/rho_0)*(1.3**2/C_Lland)*(1/(Trev+D_land+Dg_land))
a_bar_land = (g/MLW)*(-Trev-D_land-Dg_land)
x_brake = -(V_ap**2)/(2*a_bar_land)
x_total_land = x_land_airborne+x_tr+x_brake


print
print "The approach speed is:", V_ap, "m/s"
print "The airborne distance during landing is", x_land_airborne , "m"
print "The braking distance is:", x_brake, "m"
print "The total landing distance is:", x_total_land, "m"
print "Drag during landing is:", D_land, "N"
print "Lift during landing is:", L_land, "N"


#------------VERIFICATION-----
#Comment out importing the parameters first
#print "-------------Verification-----------------"
##print "Choose the thrust setting from 0 to 1"
##thrust_setting = float(raw_input("What is the thrust setting"))
##constants
#
#MTOW = 50000. #Maximum take-off weight in kg
##A = 15.91**2/30
#S = 30.
#Ae = 5.8
#rho_0= 1.225 #sea level density kg/m^3
##C_L_max = 2.3 #Maximum CL
##T = 170000. #Thrust in kN
#e = 0.85
#gamma_climb = radians(3) #degrees
#hscr = 15.24 #screen height in m
#thrust = 170000
#C_L_maxto = 2.0
#C_Lcr = 1.1
#C_D_0 = 0.07
##Intermediate calculations
#V_min = sqrt((MTOW/S)*(2/rho_0)*(1/C_L_maxto)) #Minimum speed in m/s
#V_LOF = 1.05*V_min #Lift of speed in m/s
#V = V_LOF/sqrt(2) #average speed
#CD = C_D_0 + (C_Lcr**2/(pi*Ae))
#D = CD * 0.5 * rho_0 * V**2 * S
#L = C_Lcr * 0.5 * rho_0 * V**2 * S
#
#
#Dg = 0.02*(MTOW-L) #GROUND drag with a friction coefficient of 0.02
#a_bar = (g/MTOW)*((thrust)-D-Dg) #average acceleration during ground run in m/s^2
#
##Output
#s = (V_LOF**2)/(2*a_bar) #ground run distance in m
#x_trans = (V_LOF**2/(0.15*g)) * sin(gamma_climb)
#x_climb = (hscr - ((1-cos(gamma_climb)) * (V_LOF**2/(0.15*g))))/tan(gamma_climb)
#x_total_airborne = x_trans + x_climb
#
#x_total = s + x_total_airborne
#
#print
#print "The lift of speed is:", V_LOF, "m/s"
#print "The ground run distance is:", s, "m"
#print "The airborne distance is:", x_total_airborne, "m"
#print "The total take-off distance is:", x_total, "m"
#
#
##-------------Landing performance
##V_min = sqrt((MTOW/S)*(2/rho_0)*(1/C_Lcr))
#V_ap = 1.3*V_min
#gamma_approach = radians(3)
#L_land = C_Lcr*(0.5)*rho_0*(V_ap/sqrt(2))**2*S #Lift coefficient in ground run attitude
#
#CD0_land = 0.07
#CD_land = CD0_land + (C_Lcr**2/(pi*Ae))
#D_land = CD_land*(0.5)*rho_0*(V_ap/sqrt(2))**2*S #
##R = V_ap**2/(g*0.1)
#R = (1.3**2*(((MTOW/S)*(2/rho_0)*(1/C_L_maxto))/(0.10*g)))
#x_land_airborne= R*sin(gamma_approach) + (hscr-(1-cos(gamma_approach))*R)/tan(gamma_approach) #The airspeed is assumed constant during this phase
#x_tr= 2*V_ap
#Trev = thrust*0.
#Dg_land = 0.4*(MTOW-L_land)
#x_brake=((MTOW**2)/(2*g*S))*(2/rho_0)*(1.3**2/C_L_maxto)*(1/(Trev+D_land+Dg_land))
##a_bar_land = g/MTOW*(-Trev-D_land-Dg_land)
##x_brake = -(V_ap**2)/(2*a_bar_land)
#x_total_land = x_land_airborne+x_tr+x_brake
#
#
#print
#print "The approach speed is:", V_ap, "m/s"
#print "The airborne distance during landing is", x_land_airborne , "m"
#print "The braking distance is:", x_brake, "m"
#print "The total landing distance is:", x_total_land, "m"
#print "Drag during landing is:", D_land, "N"
#print "Lift during landing is:", L_land, "N"

