from math import *
import numpy as np
import matplotlib.pyplot as plt
from parameters import *
from TWWS import S,thrust
from liftdrag import C_D_cr

#parameters
V_cr = cruise_speed(h_cr)
#V_taxi = 10.
#C_D_cr = [0.0282,0.0323,0.0253,0.0245,0.0253,0.0227]
#S = [130.6,119.6,128.,127.5,126.5,152.5]
thrust_max = thrust#[181.,181.,177.,220.,175.,187.]
T_cr = cruise_thrust(h_cr,C_D_cr,S)#[0.5*rho*V_cruise**2*C_D_cr[0]*S[0]/1000,0.5*rho*V_cruise**2*C_D_cr[1]*S[1]/1000,0.5*rho*V_cruise**2*C_D_cr[2]*S[2]/1000,0.5*rho*V_cruise**2*C_D_cr[3]*S[3]/1000,0.5*rho*V_cruise**2*C_D_cr[4]*S[4]/1000,0.5*rho*V_cruise**2*C_D_cr[5]*S[5]/1000]

#thrust specific fuel consumption ([lbm/hr/lbf])

TSFC_propfan_TO = 0.158
TSFC_propfan_CR = 0.441
TSFC_geared_TO = 0.257
TSFC_geared_CR = 0.502
TSFC_UHBP_CR = 0.9*0.42  #10% off the LeapX current gen engine
TSFC_UHBP_TO = 0.5*TSFC_UHBP_CR

#fuel flow [kg/s]

##TSFC_1_geared_TO = TSFC_geared_TO*thrust_max[0]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_1_geared_CR = TSFC_geared_CR*T_cr[0]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_1_geared_DES = TSFC_geared_TO*0.5*T_cr[0]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_2_UHBP_TO = TSFC_UHBP_TO*thrust_max[1]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_2_UHBP_CR = TSFC_UHBP_CR*T_cr[1]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_2_UHBP_DES = TSFC_UHBP_TO*0.5*T_cr[1]*1000/lbf_to_N/hr_to_s*lbm_to_kg
TSFC_3_UHBP_TO = TSFC_UHBP_TO*thrust_max*1000/lbf_to_N/hr_to_s*lbm_to_kg
<<<<<<< HEAD
TSFC_3_UHBP_CR = TSFC_UHBP_CR*T_cr*1000/lbf_to_N/hr_to_s*lbm_to_kg
TSFC_3_UHBP_DES = TSFC_UHBP_TO*0.5*T_cr*1000/lbf_to_N/hr_to_s*lbm_to_kg
=======
TSFC_3_UHBP_CR = TSFC_UHBP_CR*T_cr/lbf_to_N/hr_to_s*lbm_to_kg
TSFC_3_UHBP_DES = TSFC_UHBP_TO*0.5*T_cr/lbf_to_N/hr_to_s*lbm_to_kg
>>>>>>> af6e807275de47b92cbeaf27f70ca0418002ab59
##TSFC_4_UHBP_TO = TSFC_UHBP_TO*thrust_max[3]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_4_UHBP_CR = TSFC_UHBP_CR*T_cr[3]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_4_UHBP_DES = TSFC_UHBP_TO*0.5*T_cr[3]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_5_propfan_TO = TSFC_propfan_TO*thrust_max[4]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_5_propfan_CR = TSFC_propfan_CR*T_cr[4]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_5_propfan_DES = TSFC_propfan_TO*0.5*T_cr[4]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_6_geared_TO = TSFC_geared_TO*thrust_max[5]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_6_geared_CR = TSFC_geared_CR*T_cr[5]*1000/lbf_to_N/hr_to_s*lbm_to_kg
##TSFC_6_geared_DES = TSFC_geared_TO*0.5*T_cr[5]*1000/lbf_to_N/hr_to_s*lbm_to_kg

#distance time [km][s]

taxi_dis = 4. #GET FROM PAYLOAD-RANGE DIAGRAM
end_climbdis = 156. #GET FROM PAYLOAD-RANGE DIAGRAM
climb_dis = sqrt((39000*ft_to_km)**2+(end_climbdis-taxi_dis)**2) 
begin_descdis = 5756. #GET FROM PAYLOAD-RANGE DIAGRAM
end_descdis = 6006. #GET FROM PAYLOAD-RANGE DIAGRAM
desc_dis = sqrt((end_descdis-begin_descdis)**2+(FL*100*ft_to_km)**2)
cruise_dis = begin_descdis - end_climbdis
#taxi_time = taxi_dis/(V_taxi/1000)
cruise_time = cruise_dis/(V_cr/1000)
climb_time = climb_dis/((V_cr + V_rot)/1000/2)
desc_time = desc_dis/((V_cr + V_land)/1000/2)
total_time = cruise_time + climb_time + desc_time
nocruise_time = total_time - cruise_time

#avg specific fuel consumption [kg/s]

##cj_1_geared = (TSFC_1_geared_TO*climb_time + TSFC_1_geared_CR*cruise_time + TSFC_1_geared_DES*desc_time)/total_time
##cj_2_UHBP = (TSFC_2_UHBP_TO*climb_time + TSFC_2_UHBP_CR*cruise_time + TSFC_2_UHBP_DES*desc_time)/total_time
cj_3_UHBP = (TSFC_3_UHBP_TO*climb_time + TSFC_3_UHBP_CR*cruise_time + TSFC_3_UHBP_DES*desc_time)/total_time
##cj_4_UHBP = (TSFC_4_UHBP_TO*climb_time + TSFC_4_UHBP_CR*cruise_time + TSFC_4_UHBP_DES*desc_time)/total_time
##cj_5_propfan = (TSFC_5_propfan_TO*climb_time + TSFC_5_propfan_CR*cruise_time + TSFC_5_propfan_DES*desc_time)/total_time
##cj_6_geared = (TSFC_6_geared_TO*climb_time + TSFC_6_geared_CR*cruise_time + TSFC_6_geared_DES*desc_time)/total_time

##cj = [cj_1_geared,cj_2_UHBP,cj_3_geared,cj_4_UHBP,cj_5_propfan,cj_6_geared]

#CO2 [gCO2_eq/MJ]

CO2_camelina = 22.4
CO2_algae = 35.2 #FIND
#CO2_methane = 54.9
CO2_jatropha = 40. 
CO2_confuel = 73.1 #other source, 71.5 
CO2_soybean = 140. 

#specific energy [MJ/kg]
E_jatropha = 44.3
E_soybean = 37.
E_camelina = 44. 
E_confuel = 42.8 
E_algae = 41.  #wide range
#E_methane = 55.35

#density [kg/m^3]

rho_soybean = 917. #793 FROM RELIABLE SOURCE
rho_jatropha = 749.
rho_camelina = 753.
rho_confuel = 810.
#rho_methane = 0.664 #at 18deg
rho_algae = 864.

#cost [USD/kg]

C_jatropha = 0.45
C_camelina = 3.09/gal_to_L/rho_camelina*1000
C_confuel = 1.69/gal_to_L/rho_confuel*1000
C_algae = 10.6/gal_to_L/rho_algae*1000 #22.4 for expensive version,but higher yields
C_soybean = 0.79 #FIND
#C_methane = #FIND

#aromatics

A_soybean = 2.6
A_confuel = 18.8
A_jatropha = 10.8
A_camelina = 24.2 
A_algae = 24. #FIND

#-----------------------------------------MAIN CODE-----------------------------------------------

##design = raw_input("choose a design (1 till 6): ",)

confuel = [CO2_confuel,E_confuel,rho_confuel,C_confuel,A_confuel]
camelina = [CO2_camelina,E_camelina,rho_camelina,C_camelina,A_camelina]
jatropha = [CO2_jatropha,E_jatropha,rho_jatropha,C_jatropha,A_jatropha]
algae = [CO2_algae,E_algae,rho_algae,C_algae,A_algae]
soybean = [CO2_soybean,E_soybean,rho_soybean,C_soybean,A_soybean]

fuels = [confuel,camelina,jatropha,algae,soybean]

fuelnames = ['confuel','camelina','jatropha','algae','soybean']
costlst = []
emissionslst = []
xlst = []

fuel1 = 'confuel'
fuel2 = 'jatropha'
mix1 = 20
mix2 = 100 - mix1
#print mix1,"% of",fuel1,"has been mixed with",mix2,"% of",fuel2
aromatics = (fuels[fuelnames.index(fuel1)][4] + fuels[fuelnames.index(fuel2)][4])/2
#print "The aromatic compound is",aromatics,"%."
#if aromatics < 8.:
    #print "Aromatic compound too low (below 8)."
#elif aromatics > 25.:
    #print "Aromatic compound too high (above 25)."
#else:
c_j = cj_3_UHBP#cj[eval(design)-1]
E1 = fuels[fuelnames.index(fuel1)][1] #specific energy fuel 1
E2 = fuels[fuelnames.index(fuel2)][1] #specific energy fuel 2
emissions_per_E_1 = fuels[fuelnames.index(fuel1)][0]
emissions_per_E_2 = fuels[fuelnames.index(fuel2)][0]
sigma1 = E1*c_j*mix1/100
sigma2 = E2*c_j*mix2/100 #energy flow [MJ/s]
emissions_per_s = sigma1*emissions_per_E_1 + sigma2*emissions_per_E_2
emissionslst.append(emissions_per_s)
#print "Per second,",int(emissions_per_s),"grams of CO2eq is burnt. This is ",round(emissions_per_s*total_time/1000,1),"kg of CO2eq over a flight of",end_descdis,"km."
density1 = fuels[fuelnames.index(fuel1)][2]
density2 = fuels[fuelnames.index(fuel2)][2]
volume_needed = c_j*mix1/100*total_time/density1 + c_j*mix2/100*total_time/density2
#print "Over this distance we will need",round(cj*mix1/100*total_time/density1 + cj*mix2/100*total_time/density2,2),"m^3 of fuel."
cost1 = fuels[fuelnames.index(fuel1)][3]
cost2 = fuels[fuelnames.index(fuel2)][3]
costlst.append(c_j*mix1/100*cost1 + c_j*mix2/100*cost2)
#print "The fuel cost per s is",round(cj*mix1/100*cost1 + cj*mix2/100*cost2,2),"USD. The total fuel cost will be",round((cj*mix1/100*cost1 + cj*mix2/100*cost2)*total_time,2), "USD."

#blend = '1'#raw_input("Number of fuels blended: ",)

#if blend == '1':
##for i in range(len(fuelnames)):
##    xlst.append(i)
##    fuel = fuelnames[i]#raw_input("Fuel type (confuel,camelina,jatropha,algae or soybean): ",)
##    #mix1 = raw_input("Percentage: ",)
##    aromatics = fuels[fuelnames.index(fuel)][4]
##    #print "The aromatic compound is",aromatics,"%."
##    #if aromatics < 8.:
##        #print "Aromatic compound too low (below 8)."
##    #elif aromatics > 25.:
##        #print "Aromatic compound too high (above 25)."
##    #else:
##    c_j = cj[eval(design)-1]
##    E = fuels[fuelnames.index(fuel)][1] #specific energy
##    sigma = E*c_j #energy flow [MJ/s]
##    emissions_per_E = fuels[fuelnames.index(fuel)][0]
##    emissions_per_s = sigma*emissions_per_E
##    emissionslst.append(emissions_per_s)
##    #print "Per second,",int(emissions_per_s),"grams of CO2eq is burnt. This is ",round(emissions_per_s*total_time/1000,1),"kg of CO2eq over a flight of",end_descdis,"km."
##    density = fuels[fuelnames.index(fuel)][2]
##    #print "Over this distance we will need",round(cj*total_time/density,2),"m^3 of fuel."
##    cost = fuels[fuelnames.index(fuel)][3]
##    costlst.append(c_j*cost)
##    #print "The fuel cost per s is",round(cj*cost,2),"USD. The total fuel cost will be",round(cj*total_time*cost,2), "USD."
##    
###elif blend == '2':
##
##costlst1 = []
##emissionslst1 = []
##
##for i in range(4):
##    fuel1 = 'confuel'#raw_input("Fuel type one (confuel,camelina,jatropha,algae or soybean): ",)
##    mix1 = (i+1)*20#raw_input("Mixture (%): ",)
##    #mix1 = eval(mix1)
##    fuel2 = 'camelina'#raw_input("Fuel type two (confuel,camelina,jatropha,algae or soybean): ",)
##    mix2 = 100 - mix1
##    #print mix1,"% of",fuel1,"has been mixed with",mix2,"% of",fuel2
##    aromatics = (fuels[fuelnames.index(fuel1)][4] + fuels[fuelnames.index(fuel2)][4])/2
##    #print "The aromatic compound is",aromatics,"%."
##    #if aromatics < 8.:
##        #print "Aromatic compound too low (below 8)."
##    #elif aromatics > 25.:
##        #print "Aromatic compound too high (above 25)."
##    #else:
##    c_j = cj[eval(design)-1]
##    E1 = fuels[fuelnames.index(fuel1)][1] #specific energy fuel 1
##    E2 = fuels[fuelnames.index(fuel2)][1] #specific energy fuel 2
##    emissions_per_E_1 = fuels[fuelnames.index(fuel1)][0]
##    emissions_per_E_2 = fuels[fuelnames.index(fuel2)][0]
##    sigma1 = E1*c_j*mix1/100
##    sigma2 = E2*c_j*mix2/100 #energy flow [MJ/s]
##    emissions_per_s = sigma1*emissions_per_E_1 + sigma2*emissions_per_E_2
##    emissionslst1.append(emissions_per_s)
##    #print "Per second,",int(emissions_per_s),"grams of CO2eq is burnt. This is ",round(emissions_per_s*total_time/1000,1),"kg of CO2eq over a flight of",end_descdis,"km."
##    density1 = fuels[fuelnames.index(fuel1)][2]
##    density2 = fuels[fuelnames.index(fuel2)][2]
##    #print "Over this distance we will need",round(cj*mix1/100*total_time/density1 + cj*mix2/100*total_time/density2,2),"m^3 of fuel."
##    cost1 = fuels[fuelnames.index(fuel1)][3]
##    cost2 = fuels[fuelnames.index(fuel2)][3]
##    costlst1.append(c_j*mix1/100*cost1 + c_j*mix2/100*cost2)
##    #print "The fuel cost per s is",round(cj*mix1/100*cost1 + cj*mix2/100*cost2,2),"USD. The total fuel cost will be",round((cj*mix1/100*cost1 + cj*mix2/100*cost2)*total_time,2), "USD."
##
##costlst2 = []
##emissionslst2 = []
##
##for i in range(4):
##    fuel1 = 'confuel'#raw_input("Fuel type one (confuel,camelina,jatropha,algae or soybean): ",)
##    mix1 = (i+1)*20#raw_input("Mixture (%): ",)
##    #mix1 = eval(mix1)
##    fuel2 = 'jatropha'#raw_input("Fuel type two (confuel,camelina,jatropha,algae or soybean): ",)
##    mix2 = 100 - mix1
##    #print mix1,"% of",fuel1,"has been mixed with",mix2,"% of",fuel2
##    aromatics = (fuels[fuelnames.index(fuel1)][4] + fuels[fuelnames.index(fuel2)][4])/2
##    #print "The aromatic compound is",aromatics,"%."
##    #if aromatics < 8.:
##        #print "Aromatic compound too low (below 8)."
##    #elif aromatics > 25.:
##        #print "Aromatic compound too high (above 25)."
##    #else:
##    c_j = cj[eval(design)-1]
##    E1 = fuels[fuelnames.index(fuel1)][1] #specific energy fuel 1
##    E2 = fuels[fuelnames.index(fuel2)][1] #specific energy fuel 2
##    emissions_per_E_1 = fuels[fuelnames.index(fuel1)][0]
##    emissions_per_E_2 = fuels[fuelnames.index(fuel2)][0]
##    sigma1 = E1*c_j*mix1/100
##    sigma2 = E2*c_j*mix2/100 #energy flow [MJ/s]
##    emissions_per_s = sigma1*emissions_per_E_1 + sigma2*emissions_per_E_2
##    emissionslst2.append(emissions_per_s)
##    #print "Per second,",int(emissions_per_s),"grams of CO2eq is burnt. This is ",round(emissions_per_s*total_time/1000,1),"kg of CO2eq over a flight of",end_descdis,"km."
##    density1 = fuels[fuelnames.index(fuel1)][2]
##    density2 = fuels[fuelnames.index(fuel2)][2]
##    #print "Over this distance we will need",round(cj*mix1/100*total_time/density1 + cj*mix2/100*total_time/density2,2),"m^3 of fuel."
##    cost1 = fuels[fuelnames.index(fuel1)][3]
##    cost2 = fuels[fuelnames.index(fuel2)][3]
##    costlst2.append(c_j*mix1/100*cost1 + c_j*mix2/100*cost2)
##    #print "The fuel cost per s is",round(cj*mix1/100*cost1 + cj*mix2/100*cost2,2),"USD. The total fuel cost will be",round((cj*mix1/100*cost1 + cj*mix2/100*cost2)*total_time,2), "USD."
##
##costlst3 = []
##emissionslst3 = []
##
##for i in range(4):
##    fuel1 = 'confuel'#raw_input("Fuel type one (confuel,camelina,jatropha,algae or soybean): ",)
##    mix1 = (i+1)*20#raw_input("Mixture (%): ",)
##    #mix1 = eval(mix1)
##    fuel2 = 'algae'#raw_input("Fuel type two (confuel,camelina,jatropha,algae or soybean): ",)
##    mix2 = 100 - mix1
##    #print mix1,"% of",fuel1,"has been mixed with",mix2,"% of",fuel2
##    aromatics = (fuels[fuelnames.index(fuel1)][4] + fuels[fuelnames.index(fuel2)][4])/2
##    #print "The aromatic compound is",aromatics,"%."
##    #if aromatics < 8.:
##        #print "Aromatic compound too low (below 8)."
##    #elif aromatics > 25.:
##        #print "Aromatic compound too high (above 25)."
##    #else:
##    c_j = cj[eval(design)-1]
##    E1 = fuels[fuelnames.index(fuel1)][1] #specific energy fuel 1
##    E2 = fuels[fuelnames.index(fuel2)][1] #specific energy fuel 2
##    emissions_per_E_1 = fuels[fuelnames.index(fuel1)][0]
##    emissions_per_E_2 = fuels[fuelnames.index(fuel2)][0]
##    sigma1 = E1*c_j*mix1/100
##    sigma2 = E2*c_j*mix2/100 #energy flow [MJ/s]
##    emissions_per_s = sigma1*emissions_per_E_1 + sigma2*emissions_per_E_2
##    emissionslst3.append(emissions_per_s)
##    #print "Per second,",int(emissions_per_s),"grams of CO2eq is burnt. This is ",round(emissions_per_s*total_time/1000,1),"kg of CO2eq over a flight of",end_descdis,"km."
##    density1 = fuels[fuelnames.index(fuel1)][2]
##    density2 = fuels[fuelnames.index(fuel2)][2]
##    #print "Over this distance we will need",round(cj*mix1/100*total_time/density1 + cj*mix2/100*total_time/density2,2),"m^3 of fuel."
##    cost1 = fuels[fuelnames.index(fuel1)][3]
##    cost2 = fuels[fuelnames.index(fuel2)][3]
##    costlst3.append(c_j*mix1/100*cost1 + c_j*mix2/100*cost2)
##    #print "The fuel cost per s is",round(cj*mix1/100*cost1 + cj*mix2/100*cost2,2),"USD. The total fuel cost will be",round((cj*mix1/100*cost1 + cj*mix2/100*cost2)*total_time,2), "USD."
##
##costlst4 = []
##emissionslst4 = []
##
##for i in range(4):
##    fuel1 = 'confuel'#raw_input("Fuel type one (confuel,camelina,jatropha,algae or soybean): ",)
##    mix1 = (i+1)*20#raw_input("Mixture (%): ",)
##    #mix1 = eval(mix1)
##    fuel2 = 'soybean'#raw_input("Fuel type two (confuel,camelina,jatropha,algae or soybean): ",)
##    mix2 = 100 - mix1
##    #print mix1,"% of",fuel1,"has been mixed with",mix2,"% of",fuel2
##    aromatics = (fuels[fuelnames.index(fuel1)][4] + fuels[fuelnames.index(fuel2)][4])/2
##    #print "The aromatic compound is",aromatics,"%."
##    #if aromatics < 8.:
##        #print "Aromatic compound too low (below 8)."
##    #elif aromatics > 25.:
##        #print "Aromatic compound too high (above 25)."
##    #else:
##    c_j = cj[eval(design)-1]
##    E1 = fuels[fuelnames.index(fuel1)][1] #specific energy fuel 1
##    E2 = fuels[fuelnames.index(fuel2)][1] #specific energy fuel 2
##    emissions_per_E_1 = fuels[fuelnames.index(fuel1)][0]
##    emissions_per_E_2 = fuels[fuelnames.index(fuel2)][0]
##    sigma1 = E1*c_j*mix1/100
##    sigma2 = E2*c_j*mix2/100 #energy flow [MJ/s]
##    emissions_per_s = sigma1*emissions_per_E_1 + sigma2*emissions_per_E_2
##    emissionslst4.append(emissions_per_s)
##    #print "Per second,",int(emissions_per_s),"grams of CO2eq is burnt. This is ",round(emissions_per_s*total_time/1000,1),"kg of CO2eq over a flight of",end_descdis,"km."
##    density1 = fuels[fuelnames.index(fuel1)][2]
##    density2 = fuels[fuelnames.index(fuel2)][2]
##    #print "Over this distance we will need",round(cj*mix1/100*total_time/density1 + cj*mix2/100*total_time/density2,2),"m^3 of fuel."
##    cost1 = fuels[fuelnames.index(fuel1)][3]
##    cost2 = fuels[fuelnames.index(fuel2)][3]
##    costlst4.append(c_j*mix1/100*cost1 + c_j*mix2/100*cost2)
##    #print "The fuel cost per s is",round(cj*mix1/100*cost1 + cj*mix2/100*cost2,2),"USD. The total fuel cost will be",round((cj*mix1/100*cost1 + cj*mix2/100*cost2)*total_time,2), "USD."
##
##costlst5 = []
##emissionslst5 = []
##
##for i in range(4):
##    fuel1 = 'camelina'#raw_input("Fuel type one (confuel,camelina,jatropha,algae or soybean): ",)
##    mix1 = (i+1)*20#raw_input("Mixture (%): ",)
##    #mix1 = eval(mix1)
##    fuel2 = 'jatropha'#raw_input("Fuel type two (confuel,camelina,jatropha,algae or soybean): ",)
##    mix2 = 100 - mix1
##    #print mix1,"% of",fuel1,"has been mixed with",mix2,"% of",fuel2
##    aromatics = (fuels[fuelnames.index(fuel1)][4] + fuels[fuelnames.index(fuel2)][4])/2
##    #print "The aromatic compound is",aromatics,"%."
##    #if aromatics < 8.:
##        #print "Aromatic compound too low (below 8)."
##    #elif aromatics > 25.:
##        #print "Aromatic compound too high (above 25)."
##    #else:
##    c_j = cj[eval(design)-1]
##    E1 = fuels[fuelnames.index(fuel1)][1] #specific energy fuel 1
##    E2 = fuels[fuelnames.index(fuel2)][1] #specific energy fuel 2
##    emissions_per_E_1 = fuels[fuelnames.index(fuel1)][0]
##    emissions_per_E_2 = fuels[fuelnames.index(fuel2)][0]
##    sigma1 = E1*c_j*mix1/100
##    sigma2 = E2*c_j*mix2/100 #energy flow [MJ/s]
##    emissions_per_s = sigma1*emissions_per_E_1 + sigma2*emissions_per_E_2
##    emissionslst5.append(emissions_per_s)
##    #print "Per second,",int(emissions_per_s),"grams of CO2eq is burnt. This is ",round(emissions_per_s*total_time/1000,1),"kg of CO2eq over a flight of",end_descdis,"km."
##    density1 = fuels[fuelnames.index(fuel1)][2]
##    density2 = fuels[fuelnames.index(fuel2)][2]
##    #print "Over this distance we will need",round(cj*mix1/100*total_time/density1 + cj*mix2/100*total_time/density2,2),"m^3 of fuel."
##    cost1 = fuels[fuelnames.index(fuel1)][3]
##    cost2 = fuels[fuelnames.index(fuel2)][3]
##    costlst5.append(c_j*mix1/100*cost1 + c_j*mix2/100*cost2)
##    #print "The fuel cost per s is",round(cj*mix1/100*cost1 + cj*mix2/100*cost2,2),"USD. The total fuel cost will be",round((cj*mix1/100*cost1 + cj*mix2/100*cost2)*total_time,2), "USD."



#-----------------------------------------------------PLOTTINGS----------------------------------------------    

##fig, ax1 = plt.subplots()
##ax1.bar(xlst,costlst,align='center',color='b',width=0.2)
### Make the y-axis label, ticks and tick labels match the line color.
##ax1.set_ylabel('exp', color='b')
##ax1.tick_params('y', colors='b')
##
##ax2 = ax1.twinx()
##ax2.bar(xlst,emissionslst,align='center',color='r',width=0.2)
##ax2.set_ylabel('sin', color='r')
##ax2.tick_params('y', colors='r')
##
##fig.tight_layout()
##plt.show()

##colors = ['r','g','b','c']
##markers = ['>','d','D','^','<']
##labelss = ['kerosine','camelina', 'jatropha','algae','soybean']
##cam = ['20%kerosine-80%camelina','40%kerosine-60%camelina','60%kerosine-40%camelina','80%kerosine-20%camelina']
##
##for i in range(len(markers)):
##    plt.scatter(costlst[i],emissionslst[i],label=labelss[i],s=70,color='k',marker=markers[i])
##
##for i in range(len(colors)):
###plt.subplot(2, 1, 1)
###plt.scatter(costlst[i],emissionslst[i],label='no blends',marker='v')
##    if i == 3:
##        plt.scatter(costlst1[i],emissionslst1[i],color=colors[i],s=70,marker='v',label='blend kerosine & camelina')
##        plt.scatter(costlst2[i],emissionslst2[i],color=colors[i],s=70,marker='o',label='blend kerosine & jatropha')
##        plt.scatter(costlst3[i],emissionslst3[i],color=colors[i],s=70,marker='s',label='blend kerosine & algae')
##        plt.scatter(costlst4[i],emissionslst4[i],color=colors[i],s=70,marker='*',label='blend kerosine & soybean')
##        plt.scatter(costlst5[i],emissionslst5[i],color=colors[i],s=70,marker='x',label='blend camelina & jatropha')
##    else:
##        plt.scatter(costlst1[i],emissionslst1[i],color=colors[i],s=70,marker='v')
##        plt.scatter(costlst2[i],emissionslst2[i],color=colors[i],s=70,marker='o')
##        plt.scatter(costlst3[i],emissionslst3[i],color=colors[i],s=70,marker='s')
##        plt.scatter(costlst4[i],emissionslst4[i],color=colors[i],s=70,marker='*')
##        plt.scatter(costlst5[i],emissionslst5[i],color=colors[i],s=70,marker='x')
##plt.xlabel("USD/s")
##plt.ylabel("gCO2ev/s")
####locs, labels = plt.xticks()
####plt.xticks(np.arange(0, 5, step=1))
####plt.xticks(np.arange(5), ('Confuel', 'Camelina', 'Jatropha', 'Algae', 'Soybean'),rotation=20)
##ax = plt.subplot(111)
##box = ax.get_position()
##ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
##ax.legend(bbox_to_anchor=(1, 1))
##plt.grid()
####
####plt.subplot(2, 1, 2)
####plt.bar(xlst,emissionslst,align='center',width=0.2)
####plt.ylabel("gCO2eq/MJ")
####locs, labels = plt.xticks()
####plt.xticks(np.arange(0, 5, step=1))
####plt.xticks(np.arange(5), ('Confuel', 'Camelina', 'Jatropha', 'Algae', 'Soybean'),rotation=20)
######ax = plt.subplot(111)
######box = ax.get_position()
######ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
######ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
####plt.grid()
####
##plt.show()


