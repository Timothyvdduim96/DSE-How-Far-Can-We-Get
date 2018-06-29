# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 18:15:36 2018

@author: mrvan
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt
from parameters import *



Vmax = cruise_speed(value("h_cr"))*sqrt(0.316/1.225)*1.943844  #cruise speed in keas
M_cr = 0.79
MTOW = value("MTOW") #[kg]
OEW = value("OEW")   #[kg]
W_TO = MTOW * 2.2046 #take-off weight in pounds
W_e = OEW * 2.2046 #empty weight in pounds
inf12 = 1.095818 #inflation factor 2012 to 2018
oplife = 30. # years operational
flyhours = 4380 #flying hours per year
fly_block = 1.175 #ratio block hours flying hours
blockhours = 5146.5
flytime = 2.
t_b = 2.35 #block time
T_to_N = 213000./2. #take of thrust [N]
T_to = T_to_N * 0.2248089 # [lbs]
T_cr_kN = (42309./2.) # Cruise thrust per engine [kN]
T_cr = T_cr_kN*224.8089
SFC_met = 5.8/2.  # specific fuel consumption per engine [mg/N/s]
SFC = 0.378#SFC_met * 0.03538 # lb/hr/lb
R_des = 1800. # [Range in km]
R = R_des*0.621371192

TC = inf12*425*erf((W_e-10000)/450000)*1000000  # market price
C_e = inf12*1.2*(1+(T_cr**0.88)/(SFC**2.58))
V_b = R/t_b #block speed [mph]
r_i = 0.02  #insurance premium rate
L_mhc = 6 + 0.05*(W_e/1000.) - 630./(W_e/1000.+120) # labor man-hours per flight cycle
L_mhf = 0.59*L_mhc
U = blockhours  #utilization
r_L = 40*inf12 # labor cost per hour
t_f = flytime
t_dep = 30 #depreciation period
LF = 0.94
N_p = 240.


# DOC per airmile
C_crew = inf12*(0.349*W_TO/1000. + 697.)/V_b
C_ins = (r_i*TC)/(U*V_b)
C_main_af_labor = (L_mhf*t_f + L_mhc)*r_L*sqrt(M_cr)/(V_b*t_b)
C_main_af_material = ((TC-2*C_e)*(3.08*t_f+6.24)*0.000001)/(V_b*t_b)
C_main_eng_labor = ((r_L*2)/(V_b*t_b))*((0.6+0.027*T_to/1000.)*1.08*t_f + (0.065 + 0.03*T_to/1000.))
C_main_eng_material = (2*2*(C_e/100000)*(1.25*t_f+1))/(V_b*t_b)
C_dep = (0.9*TC-0.3*2*C_e)/(U*V_b*t_dep)

# IOC per airmile
IOC = inf12*(R**-0.41)*((1.42E-4)*W_TO + (0.13 + 1.4*LF)*N_p-4.4)

# DOC per block hour
C_crew_b = C_crew*V_b
C_ins_b = C_ins*V_b
C_main_af_labor_b = C_main_af_labor*V_b
C_main_af_material_b = C_main_af_material*V_b
C_main_eng_labor_b = C_main_eng_labor*V_b
C_main_eng_material_b = C_main_eng_material*V_b
C_dep_b = C_dep*V_b
C_fuel_b = 1651.

DOC_b = C_crew_b + C_ins_b + C_main_af_labor_b  + C_main_af_material_b + C_main_eng_labor_b +  C_main_eng_material*V_b + C_dep_b + C_fuel_b 
IOC_b = IOC*V_b

