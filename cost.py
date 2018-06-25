# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:12:20 2018

@author: mrvan
"""
from math import *
import numpy as np
import matplotlib.pyplot as plt
from parameters import *


Tmax = 1
Tturbine =1350.
Q = 500.
ff = 1.5 #fudge factor
Vmax = cruise_speed(value("h_cr"))*3.6 #cruise speed in km/hr
MTOW = value("MTOW")
OEW = value("OEW")
FTA = 3. #number of test flights
inf99 = 1.51 #inflation factor 1999 to 2018
inf95 = 1.651
T_cr_kN = (42309./2.) # Cruise thrust per engine [kN]
T_cr = T_cr_kN*224.8089
SFC_met = 5.8/2  # specific fuel consumption per engine [mg/N/s]
SFC = 0.378#SFC_met * 0.03538
oplife = 30 # years operational
flyhours = 4380 #flying hours per year
fly_block = 1.175 #ratio block hours flying hours
blockhours = 5146.5


H_E = ff*7.53*OEW**0.777*Vmax**0.894*Q**0.163
H_T = ff*10.5*OEW**0.777*Vmax**0.696*Q**0.263
H_M = ff*15.2*OEW**0.82*Vmax**0.484*Q**0.641
H_Q = ff*0.133*H_M

C_D = inf99*48.7*OEW**0.63*Vmax**1.3
C_F = inf99*1408*OEW**0.325*Vmax**0.822*FTA**1.21
C_M = inf99*22.6*OEW**0.921*Vmax**0.621*Q**0.799
C_eng = 3095599
C_av = 4643398

R_E = inf99* 1.3*86  #1999 dollar
R_T = inf99* 1.3*88
R_Q = inf99* 1.3*81
R_M = inf99*1.3*73


TC = 76200000  # total aircraft market price in 2018$ (factory price)
vf = (T_cr**0.88)*(SFC**-2.58)  #engine value factor
C_e = (0.4*vf+0.6)*1000000*inf95 #engine cost
C_af = TC-C_e


spares = 0.1*C_af+0.3*2*C_e  #spares cost
TC_inv = TC + spares  #total investment cost  (Purchase price)

depr = 0.1  #pecentage depreciation of TC_inv
interest = 0.054 #interest on investment cost
insurance = 0.01
C_depr_year = (1-depr)*TC_inv/oplife #depreciation cost per year
C_ins_year = insurance*TC
C_int_year = interest*TC_inv
C_standing_year = C_depr_year + C_ins_year + C_int_year #standing charge per year
C_standing = C_standing_year/blockhours  # standing charge per flying hour



#DOC
C_crew = 54*(V_cr*3.6*MTOW/(10**5))**0.3+122  # crew cost per block hour in 1999$ (Raymer)
C_crew_now = C_crew*inf99

print (vf)

Cost = H_E*R_E + H_T*R_T + H_T*R_T + H_M*R_M + H_Q*R_Q + C_D + C_F + C_M + 2*C_e +C_av


