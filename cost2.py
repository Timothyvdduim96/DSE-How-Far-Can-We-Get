# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:44:08 2018

@author: mrvan
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt
from parameters import *



Vmax = cruise_speed(value("h_cr"))*sqrt(0.316/1.225)*1.943844  #cruise speed in keas
MTOW = value("MTOW") #[kg]
OEW = value("OEW")   #[kg]
W_TO = MTOW * 2.2046 #take-off weight in pounds
inf99 = 1.51 #inflation factor 1999 to 2018
inf95 = 1.651
inf89 = 2.029 
oplife = 30. # years operational
flyhours = 4380 #flying hours per year
fly_block = 1.175 #ratio block hours flying hours
blockhours = 5146.5
T_to_N = 213000./2. #take of thrust [N]
T_to = T_to_N * 0.2248089 # [lbs]


N_rdte = 5. #number of test flight planes
N_program = 500 # total number of airplanes produced
N_m = N_program - N_rdte
N_pax = 240.
F_diff = 1.8 #technology factor
F_cad = 0.8  #cad experience
W_ampr = 10**(0.1936 + 0.8645*log10(W_TO))
R_e = 60.
MHR_aed = 0.0396*W_ampr**0.791*Vmax**1.526*N_rdte**0.183*F_diff*F_cad
C_aed = MHR_aed*R_e

CEF = 3.1 #1989
C_dst = 0.008325*W_ampr**0.873*Vmax**1.89*N_rdte**0.346*CEF*F_diff


N_r = 0.33
R_t = 45.
MHR_tool = 4.0127*W_ampr**0.764*Vmax**0.899*N_rdte**0.178*N_r**0.066*F_diff
C_tool = MHR_tool*R_t
F_mat = 3. #carbon composite cost factor
C_mat = 37.632*F_mat*W_ampr**0.689*Vmax**0.624*N_rdte**0.792
R_m = 35.
MHR_man = 28.984*W_ampr**0.74*Vmax**0.543*N_rdte**0.524*F_diff
C_man = MHR_man*R_m
C_qc = 0.13*C_man
C_avionics = 2670000. #avionics cost:update!
C_e = 10**(2.3044+0.8858*log10(T_to))
N_st = 2.
C_ea = (C_e*2 + C_avionics)*(N_rdte - N_st)
C_fta = C_ea + C_man + C_mat + C_tool + C_qc

F_obs = 1.
C_fto = 0.001244*W_ampr**1.16*Vmax**1.371*(N_rdte-N_st)**1.281*CEF*F_diff*F_obs

F_tsf = 0.2
F_pro = 0.1
F_fin = 0.1
#C_tsf = F_tsf*C_RDTE
#C_pro = F_pro*C_RDTE
#C_fin = F_fin*C_RDTE

C_RDTE = (C_aed + C_dst + C_fta + C_fto)/(1-F_tsf-F_pro-F_fin)

CEF_1973 = 1.14
N_prot = 2.
C_prot = 1115400*W_ampr**0.35*N_prot**0.99*CEF/CEF_1973


R_t_m = R_t
N_r_m = 40.  # aircraft produced per month
MHR_tool_program = 4.0127*W_ampr**0.764*Vmax**0.899*N_program**0.178*N_r_m**0.066*F_diff
C_tool_m = MHR_tool_program*R_t_m - C_tool
C_mat_program = 37.632*F_mat*W_ampr**0.689*Vmax**0.624*N_program**0.792
C_mat_m = C_mat_program - C_mat
R_m_m = R_m
MHR_man_program = 28.984*W_ampr**0.740*Vmax**0.543*N_program**0.524*F_diff
C_man_m = MHR_man_program*R_m_m - MHR_man*R_m
C_qc_m  = 0.13*C_man_m
F_int = 2000.
C_int_m = F_int*N_pax*N_m
C_e_m = C_e
C_avionics_m = C_avionics
C_ea_m = (C_e_m*2 +  C_avionics_m)*N_m
C_apc_m = C_ea_m + C_int_m + C_man_m + C_mat_m + C_tool_m + C_qc_m
MHR_aed_program = 0.0396*W_ampr**0.791*Vmax**1.526*N_program**0.183*F_diff*F_cad
R_e_m = R_e
C_aed_m = MHR_aed_program*R_e_m - C_aed

F_fin_m = 0.1
#C_fin_m = F_fin_m*C_MAN

C_MAN = (C_aed_m + C_apc_m) / (1-F_fin_m)
C_PRO = 0.1*C_MAN
C_ACQ = C_MAN + C_PRO
AEP = (C_ACQ+C_RDTE)*inf89/N_m #AEP in 2018

print (T_to)