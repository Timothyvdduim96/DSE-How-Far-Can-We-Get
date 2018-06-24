# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:09:41 2018

@author: mrvan
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt
from parameters import *

"""
#--------------------------PARAMETERS--------------------------------
"""

#--------------------------parameters---------------------------------

V_cr = cruise_speed(value("h_cr"))
thrust_max = value("thrust")
T_cr = 42309.#cruise_thrust(value("h_cr"),value("C_D_cr"),value("S"))

"""
#------------------------FUEL CONSUMPTION----------------------------
"""

#---------thrust specific fuel consumption ([lbm/hr/lbf])-------------

TSFC_UHBP_CR = 0.9*0.42  #10% off the LeapX current gen engine
TSFC_UHBP_TO = 0.31*V_cr**2/(1.225*(V_cr - 79.8)**2)*TSFC_UHBP_CR

#---------------------fuel consumption [kg/s]--------------------------

FC_3_UHBP_TO = TSFC_UHBP_TO*thrust_max*1000/lbf_to_N/hr_to_s*lbm_to_kg
FC_3_UHBP_CR = TSFC_UHBP_CR*T_cr/lbf_to_N/hr_to_s*lbm_to_kg
FC_3_UHBP_DES = TSFC_UHBP_CR*0.5*T_cr/lbf_to_N/hr_to_s*lbm_to_kg

#--------------------------distance [km]--------------------------------

taxi_dis = 4. #GET FROM PAYLOAD-RANGE DIAGRAM
end_climbdis = 156. #GET FROM PAYLOAD-RANGE DIAGRAM
begin_descdis = 5756. #GET FROM PAYLOAD-RANGE DIAGRAM
end_descdis = 6006. #GET FROM PAYLOAD-RANGE DIAGRAM

climb_dis = sqrt((39000*ft_to_km)**2+(end_climbdis-taxi_dis)**2) 
desc_dis = sqrt((end_descdis-begin_descdis)**2+(value("FL")*100*ft_to_km)**2)
cruise_dis = begin_descdis - end_climbdis

#------------------------------time [s]---------------------------------

cruise_time = cruise_dis/(V_cr/1000)
climb_time = climb_dis/((V_cr + value("V_rot"))/1000/2)
desc_time = desc_dis/((V_cr + value("V_land"))/1000/2) #reconsider
total_time = cruise_time + climb_time + desc_time
nocruise_time = total_time - cruise_time

#--------------avg specific fuel consumption [kg/s]----------------------

c_j = (FC_3_UHBP_TO*climb_time + FC_3_UHBP_CR*cruise_time + FC_3_UHBP_DES*desc_time)/total_time

"""
#------------------------------DATA FUELS--------------------------------
"""

#--------------------emissions per MJ [gCO2/MJ]--------------------------

CO2_camelina = 22.4
CO2_algae = 35.2
CO2_jatropha = 40. 
CO2_confuel = 73.1
CO2_soybean = 140. 

#---------------------specific energy [MJ/kg]----------------------------

E_jatropha = 44.3
E_soybean = 37.
E_camelina = 44. 
E_confuel = 42.8 
E_algae = 41.  #wide range

#--------------------------density [kg/m^3]-------------------------------

rho_soybean = 917. #793 FROM RELIABLE SOURCE
rho_jatropha = 749.
rho_camelina = 753.
rho_confuel = 810.
rho_algae = 864.

#----------------------------cost [USD/kg]---------------------------------

C_jatropha = 0.45
C_camelina = 3.09/gal_to_L/rho_camelina*1000
C_confuel = 1.69/gal_to_L/rho_confuel*1000
C_algae = 10.6/gal_to_L/rho_algae*1000 #22.4 for expensive version,but higher yields
C_soybean = 0.79

#-------------------------------aromatics----------------------------------

A_soybean = 2.6
A_confuel = 18.8
A_jatropha = 10.8
A_camelina = 24.2 
A_algae = 24.

"""
#--------------------------------MAIN CODE--------------------------------
"""

#---------------------------------lists-------------------------------------

confuel = [CO2_confuel,E_confuel,rho_confuel,C_confuel,A_confuel]
camelina = [CO2_camelina,E_camelina,rho_camelina,C_camelina,A_camelina]
jatropha = [CO2_jatropha,E_jatropha,rho_jatropha,C_jatropha,A_jatropha]
algae = [CO2_algae,E_algae,rho_algae,C_algae,A_algae]
soybean = [CO2_soybean,E_soybean,rho_soybean,C_soybean,A_soybean]

fuels = [confuel,camelina,jatropha,algae,soybean]

fuelnames = ['confuel','camelina','jatropha','algae','soybean']

def emissions(fuel):
    CO2 = fuels[fuelnames.index(fuel)][0]                   #gCO2/MJ
    E = fuels[fuelnames.index(fuel)][1]                     #MJ/kg
    density = fuels[fuelnames.index(fuel)][2]               #kg/m^3
    C = fuels[fuelnames.index(fuel)][3]                     #USD/kg
    A = fuels[fuelnames.index(fuel)][4]                     #aromatic compound

    Emissions_per_kg = CO2*E/1000                           #kgCO2/kg
    Emissions_per_s = Emissions_per_kg*c_j                  #kgCO2/s
    Emissions_total = Emissions_per_s*total_time            #kgCO2
    Fuelvol_needed = c_j*total_time/density                 #m^3
    Fuelcost_per_s = c_j*C                                  #USD/s

    return Fuelcost_per_s,Emissions_per_s,Emissions_per_kg,Emissions_total
    
def emissions_blend(fuel_1,mix_1,fuel_2,mix_2):
    CO2_1 = fuels[fuelnames.index(fuel_1)][0]                                                               #gCO2/MJ
    E_1 = fuels[fuelnames.index(fuel_1)][1]                                                                 #MJ/kg
    density_1 = fuels[fuelnames.index(fuel_1)][2]                                                           #kg/m^3
    C_1 = fuels[fuelnames.index(fuel_1)][3]                                                                 #USD/kg
    A_1 = fuels[fuelnames.index(fuel_1)][4]                                                                 #aromatic compound

    CO2_2 = fuels[fuelnames.index(fuel_2)][0]                                                               #gCO2/MJ
    E_2 = fuels[fuelnames.index(fuel_2)][1]                                                                 #MJ/kg
    density_2 = fuels[fuelnames.index(fuel_2)][2]                                                           #kg/m^3
    C_2 = fuels[fuelnames.index(fuel_2)][3]                                                                 #USD/kg
    A_2 = fuels[fuelnames.index(fuel_2)][4]                                                                 #aromatic compound

    Emissions_per_kg = CO2_1*E_1*mix_1/100/1000 + CO2_2*E_2*mix_2/100/1000                                  #kgCO2/kg
    Emissions_per_s = Emissions_per_kg*c_j                                                                  #kgCO2/s
    Emissions_total = Emissions_per_s*total_time                                                            #kgCO2
    Fuelvol_needed = c_j*total_time*mix_1/100/density_1 + c_j*total_time*mix_2/100/density_2                #m^3
    Fuelcost_per_s = c_j*mix_1/100*C_1 + c_j*mix_2/100*C_2                                                  #USD/s

    return Fuelcost_per_s,Emissions_per_s,Emissions_per_kg,Emissions_total

