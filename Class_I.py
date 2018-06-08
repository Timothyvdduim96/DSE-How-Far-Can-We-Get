##-------------------------------------------
##------ import libraries and inputs --------
##-------------------------------------------
import numpy as np
import scipy as sp
import math

##-------------------------------------------
##----------- converstion factors -----------
##-------------------------------------------
mft        = 3.2808399        # conversion factor meters to feet
kglbs      = 2.20462262       # conversion factor kilograms to pounds
sqmsqft    = 10.7639104       # conversion factor square meters to square feet
mskts      = 1.94384449       # conversion factor meters per seconds to knots
degrad     = 0.0174532925     # conversion factor degrees to radians
kmnm       = 0.539956803      # conversion factor kilometers to nautical miles
Nlbs       = 0.224808943      # conversion factor newtons to pounds
papsf      = 0.02089          # conversion factor pascal to pound-force per square foot
kgmlbsgall = 0.00834540445    # conversion factor for kilogram per cubic meter to pounds per gallon
papsi      = 0.000145037738   # conversion factor for pascal to pounds-force per square inch

##-------------------------------------------
##---- Class I weight estimation roskam -----
##-------------------------------------------
##
##----- Inputs -----
##
#Aerodynamic inputs
Range_cruise  = 1400000         # range for cruise [m]
Range_cruise2 = 250000          # range for cruise 2 [m]
V_cruise      = 230.556         # cruise speed [m/s]
LoverD        = 20.61138051     # lift to drag ratio [-]
g             = 9.80665         # gravitational constant [m/s^2]
C_j           = 1.31595*10**-5  # specific fuel consumption [?]
LoverD_loiter = 23.79997217     # lift to drag ratio for loiter [-]
C_l_loiter    = 0.785399082     # lift coefficient for loiter [-]
C_d_loiter    = 0.033           # drag coefficient for loiter [-]
C_d0          = 0.0165          # zero lift drag coefficient for loiter [-]
e             = 0.85            # oswald efficiency factor [-]
A             = 14.0            # aspect ratio [-]
C_fe          = 0.003           # ??
S_wetoverS    = 5.5             # ?? [-]
fuel_unused   = 0.003           # ?? [?]
#Linear regression
a = 0.5011 #linear regression coefficient
b = 36338  #linear regression coefficient
#Fuel fractions
ff_enginestart = 0.99         # fuel fraction for engine start [-]
ff_taxi        = 0.99         # fuel fraction for taxi [-]
ff_takeoff     = 0.995        # fuel fraction for take-off [-]
ff_climb1      = 0.98         # fuel fraction for climb 1 [-]
ff_cruise1     = 0.96269425   # fuel fraction for cruise 1 [-]
ff_descend1    = 0.99         # fuel fraction for descend 1 [-]
ff_climb2      = 0.98         # fuel fraction for climb 2 [-]
ff_cruise2     = 0.99323381   # fuel fraction for cruise 2 [-]
ff_loiter      = 0.99028733   # fuel fraction for loiter [-]
ff_descend2    = 0.99         # fuel fraction for descend 2 [-]
ff_landing     = 0.992        # fuel fraction for landing [-]
#payload
n_pax_max = 240.0     # number of passengers [-]
w_pax     = 90.0      # weight of one passenger [kg]
f_load    = 0.9433    # passenger load factor [-]
#crew
n_pil = 2.0    # number of pilots [-]
n_cc  = 5.0    # number of cabin crew members [-]
w_pil = 109.0  # weight of one pilot [kg]
w_cc  = 95.25  # weight of one cabin crew member  [kg]        
##
##----- Equations -----
##
# payload weights
PL_max = n_pax_max*w_pax        # maximum payload weight [kg]
PL_max_N = PL_max*g             # maximum payload weight [N]
payload = PL_max*f_load         # actual payload weight [kg]
PL_N = payload*g                # actual payload weight [N]
n_pax_act = int(payload/w_pax)  # actual number of passengers [-]
#crew weights
W_crew = n_pil*w_pil+n_cc*w_cc  # crew weight [kg]
W_crew_N = W_crew*g             # crew weight [N]
#fuel fractions
M_ff = ff_enginestart*ff_taxi*ff_takeoff*ff_climb1*ff_cruise1*ff_descend1*ff_climb2*ff_cruise2*ff_loiter*ff_descend2*ff_landing   # product of all fuel fractions [-]
W_f_fraction = 1-M_ff                                                                                                             # fuel weight fraction [-]
#take-off weight
W_to_N = (PL_N+W_crew_N+b)/(1-(a+W_f_fraction+fuel_unused))   # take-off weight [N]
MTOW1 = W_to_N/g                                              # take-off weight [kg]
#aircraft weights
W_fuel = W_f_fraction*MTOW1   # fuel weight [kg]
W_fuel_N = W_fuel*g           # fuel weight [N]
W_empty_N = a*W_to_N+b         # empty weight [N]
W_empty1 = W_empty_N/g        # empty weight [kg]  
W_oew_N = W_empty_N+W_crew_N  # operational empty weight [N]
OEW1 = W_oew_N/g              # operational empty weight [kg]
##
##----- Output -----
##
#print 'Take-off weight =', MTOW, '[kg]'
#print 'Operational empty weight =', OEW, '[kg]'
#print 'Empty weight =', W_empty, '[kg]'
#print 'Crew weight =', W_crew, '[kg]'
#print 'Fuel weight =', W_fuel, '[kg]'
#print 'Payload weight =', payload, '[kg]'
#print 'actual number of passengers =', N_pax_act
#print
#raw_input('press enter to close')

string_class_I = ["MTOW1","OEW1","W_empty1","W_crew","W_fuel","payload","N_pax_act"]
