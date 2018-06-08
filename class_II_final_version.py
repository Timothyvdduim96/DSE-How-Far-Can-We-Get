##--------------------------------------
##import libraries
##--------------------------------------
import numpy as np
import scipy as sp
import math
from parameters import *

##--------------------------------------
##converstion factors
##--------------------------------------
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


##
##----- Inputs -----
##
# Total weight list
W_totros = []   # empty list for all weight groups from Roskam method
W_tottor = []   # empty list for all weight groups from Torenbeek method
# Wing weight
S           = 127.95*sqmsqft     # wing area [sqft]
A           = 14.0               # aspect ratio 
M_max       = 0.82               # max mach number at sea level 
MTOW        = 69176.55*kglbs     # take-off weight [lbs]
n_ult       = 3.75               # ultimate load factor
t_c         = 0.18               # thickness to chord 
lambdac_2   = 0.63               # wing half-chord sweep angle [rad]
taper       = 0.27               # taper ratio
k_wg        = 0.0017             # constant
W_zf        = 59646.88*kglbs     # zero fuel weight [lbs]
t_r         = 0.8586*mft         # wing root thickness [ft]
b           = 42.33*mft          # wingspan [ft]
# Empennage weight
Sh               = 17.4*sqmsqft     # horizontal tail area [ft]
b_h              = 8.75*mft         # horizontal tail span [ft]
t_r_h            = 0.3975*mft       # horizontal tail max root thickness [ft]
MAC              = 3.36*mft         # mean aerodynamic chord [ft]
lh               = 25.73*mft        # distance wing quarter chord to horizontal tail quarter chord [ft]
z_h              = 0.0              # distance horizontal tail to vertical tail root [ft]
b_v              = 6.8*mft          # vertical tail span [ft]
Sv               = 25.9*sqmsqft     # vertical tail area [sqft]
lv               = 20.947           # distance wing quarter chord to vertical tail quarter chord [ft]
Sr               = 0.26*Sv         # rudder area [sqft]
A_v              = 1.8              # vertical tail aspect ratio
lambda_v         = 0.45             # vertical tail taper ratio
sweep_v          = 40*degrad        # vertical tail quarter chord sweep angle [rad]
k_h              = 1.1              # constant horizontal tail
sweep_h          = 33.0*degrad      # horizontal tail sweep
k_v              = 1.0              # constant vertical tail
# Fuselage weight
K_inl          = 1.0                 # correction factor for inlets not located on fuselage
qbar_D         = 77473.24003*papsf   # design dive dynamic pressure [psf]
pi             = np.pi               #pi
d_ext_fus      = 4.0*mft             #fuselage diameter
l_fus          = 44.85*mft           #fuselage length
ratio_nosecone = 1.5                 #fineness ratio nosecone
ratio_tailcone = 3.5                 #fineness ratio tailcone
k_fus          = 0.0242676           #correction factor for pressurized fuselage and main gear attached to fuselage
V_D            = 355.65*mskts        #dive speed [kts]
N_inl = 2.0                # number of inlets
A_inl = 3.858*sqmsqft      # capture area per inlet in [sqft]
l_n   = 1.6*mft            # nacelle length from inlet lip to compressor face [ft]
P_2   = 147077.1891*papsi  # max static pressure at engine compressor face [psi] (typically from 15 to 50)
# Landing gear weight
EGTS = 300*kglbs        # electric green taxiing system
W_g  = 39064.07*kglbs   # OEW
# power plant weight
    # Engine
n_e   = 2.0        # number of engines
W_eng = 5000.0     # weight of one engine
    # Fuel system
N_t    = 8.0                # number of separate fuel tanks
W_fuel = 9529.68*kglbs      # mission fuel weight (including reserves) [lbs]
K_fsp  = 810.0*kgmlbsgall   # density of fuel [lbs/gal]
    # propulsion system
T = (220000.0)*Nlbs     #take-off static thrust per engine [lbs]
F_to = T/2
# fixed equipment weight
n_pil = 2.0           # number of pilots
battery = 25.5*kglbs  # second battery unit 
volume_cabin = 254.12*mft**3    # passenger cabin volume [ft^3]
N_cr    = 7.0              # number of crew
N_pax   = 240.0            # number of passengers    
K_bc    = 0.0646        # factor for preload provisions (check with melkert)
l_cargo = 19.55*mft  # length of cargo hold
w_cargo = 1.43*mft   # width of cargo hold floor   
N_fdc   = n_pil          # pilot seats
N_cc    = 5.0            # cabin crew seats
K_lav   = 0.31           # factor for short range aircraft
K_buf   = 1.02           # factor for short range aircraft
P_c     = 75262.4*papsi  # cabin pressure set at pressure of 8000ft
W_empty = 38369.82*kglbs   # aircraft empty weight
#maximum take-off weight
payload = 20375.28   #payload weight [kg]
fuel    = 9529.68    #fuel weight [kg]
# Avionics group
W_empty = 38369.815      #empty weight
R = 6254*kmnm            #maximum range/ferry range

##--------------------------------------------------
##----- Class II weight estimation - Torenbeek -----
##--------------------------------------------------
'''!!!!!all weights should be in pounds!!!!!'''
'''!!!!!all lengths should be in feet!!!!!'''
##
##----- Equations -----
##
# Wing group
W_wg = k_wg*(W_zf)**0.7*(S)**0.3*(n_ult)**0.55*(t_r)**-0.3*(b/np.cos(lambdac_2))**1.05*(1+np.sqrt((6.25*np.cos(lambdac_2))/b))   #fuselage group weight
W_wg = W_wg*0.95    #correction for wing mounted engines
# Fuselage group
F = l_fus/d_ext_fus                                   #fuselage fineness ratio
S_g = pi*d_ext_fus*l_fus*(1-(ratio_nosecone/(3*F))-(ratio_tailcone/(2*F)))    #gross wetted area
W_fus = k_fus*(S_g)**1.2*np.sqrt(V_D*(lh/(2*d_ext_fus))) #fuselage group weight
# Landing gear group
W_MG = 40.+0.16*W_g**0.75+0.019*W_g+1.5*10**-5*W_g**1.5  #main landing gear weight
W_NG = 20.+0.10*W_g**0.75+2*10**-6*W_g**1.5             #nose gear weight
W_LG = W_MG+W_NG+EGTS                           #total landing gear weight + EGTS system
# Tail group
W_ht = k_h*Sh*(2.+4.15*math.erf((((Sh)**0.2*V_D)/((10)**3*np.sqrt(np.cos(sweep_h))))-0.65))   #horizontal tail weight
W_vt = k_v*Sv*(2.+4.15*math.erf((((Sv)**0.2*V_D)/((10)**3*np.sqrt(np.cos(sweep_v))))-0.65))   #vertical tail weight
W_t = W_ht+W_vt #total tail weight
# Propulsion group
W_e = 2.7*(F_to)**0.75      #engine weight for one engine
W_pg = 10.*(n_e*W_e)**0.8   #propulsion goup weight
# Nacelle group
W_ng = 4.5*(n_e*W_e)**0.9-W_pg #nacelle group weight
# Flight controls group
W_fc = 1.44*(W_g)**0.625   #flight controls group weight
# Instruments group
W_ig = 0.55*(W_g)**0.6   #instruments group weight
# Hydraulic and pneumatic group
W_hp = 0.1*(W_g)**0.8   #hydraulic and pneumatic group weight
# Electrical group
W_el = 9*(W_g)**0.473+25.5*kglbs #electrical group weight + extra battery unit
# Avionics group
W_av = 0.575*(W_empty)**0.55*(R)**0.25   #avionics group weight
# Equipment and furnishing group
W_ef = 0.211*(W_zf)**0.91   #equipment and furnishing group weight
# Air conditioning and anti-icing group
W_aci = 5*np.sqrt(W_g)


##
##----- output -----
##
# Wing group
W_tottor.append(W_wg)
# Fuselage group
W_tottor.append(W_fus)
# Landing gear group
W_tottor.append(W_LG)
# Tail group
W_tottor.append(W_t)
# Propulsion group
W_tottor.append(W_pg)
# Nacelle group
W_tottor.append(W_ng)
# Flight control group
W_tottor.append(W_fc)
# Instruments group
W_tottor.append(W_ig)
# Hydraulic and pneumatic group
W_tottor.append(W_hp)
# Electrical group
W_tottor.append(W_el)
# Avionics group
W_tottor.append(W_av)
# Equipment and furnishing group
W_tottor.append(W_ef)
# Air conditioning and anti-icing group
W_tottor.append(W_aci)
 

##--------------------------------------
##total weights
##--------------------------------------
totalweighttor = sum(W_tottor)
print
#print 'the operational empty weight =', totalweightlbs, '[lbs]'
totalweighttor = totalweighttor/kglbs
payload = 20375.28 #payload weight [kg]
fuel = 9529.67798556 #fuel weight [kg]
W_takeofftor = totalweighttor+payload+fuel



##-------------------------------------------
##---- Class II weight estimation roskam ----
##-------------------------------------------
##
##----- Equations -----
##
# Wing weight
W_w = (0.00428*(S**0.48)*(A)*(M_max**0.43)*(MTOW*n_ult)**0.84*taper**0.14)/((100*t_c)**0.76*(np.cos(lambdac_2))**1.54)
# Fuselage weight
W_fus = 10.43*(K_inl)**1.42*(qbar_D/100)**0.283*(MTOW/1000)**0.95*(l_fus/d_ext_fus)**0.71
# Landing gear weight
W_lg = 62.21*(MTOW/1000)**0.84+EGTS
# Empennage weight
W_h = 0.0034*((MTOW*n_ult)**0.813*(Sh)**0.584*(b_h/t_r_h)**0.033*(MAC/lh)**0.28)**0.915  # horizontal tail weight
W_v = 0.19*((1+(z_h/b_v))**0.5*(MTOW*n_ult)**0.363*(Sv)**1.089*(M_max)**0.601*(lv)**-0.726*(1+(Sr/Sv))**0.217*(A_v)**0.337*(1+lambda_v)**0.363*(np.cos(sweep_v))**-0.484)**1.014   # vertical tail weight
W_emp = W_h+W_v  # total empennage weight
# Power plant weight
W_e = n_e*W_eng                                            # engine weight
W_ai = 0                                                   # air induction system weight included in nacelle weight
W_fs = 80*(n_e+N_t-1)+15*(N_t)**0.5*(W_fuel/K_fsp)**0.333  # fuel system weight
W_ec = 88.46*((l_fus+b)*(n_e/100))**0.294                  # engine controls weight
W_ess = 38.93*(W_e/1000)**0.918                            # engine starting system
W_p = W_ec+W_ess                                           # propulsion weight
W_pp = W_e+W_ai+W_fs+W_p                                   # power plant weight
# Nacelle weight
W_n = 3.0*(N_inl)*((A_inl)**0.5*(l_n)*(P_2))**0.731  
# fixed equipment weight
W_fc = 56.01*(MTOW*(qbar_D/100000))**0.576                                                                                    # flight control system weight
W_hp = 0.009*MTOW                                                                                                             # hydraulic and pneumatic system weight
W_aie = n_pil*(15+0.032*(MTOW/1000))+n_e*(5+0.006*(MTOW/1000))+0.15*(MTOW/1000)+0.012*MTOW                                    # instrumentation, avionics and electronics weight
W_els = 1.163*((W_fs+W_aie)/1000)**0.506+battery                                                                              # electrical system weight
W_api = 469*(volume_cabin*(N_cr+N_pax)/10000)**0.419                                                                                 # air conditioning, pressurization and anti-icing system
W_ox = 7*(N_cr+N_pax)**0.702                                                                                                  # oxygen system
S_ff = l_cargo*w_cargo                                                                                                        # cargo hold floor area [sqft]
W_bc = 3*S_ff                                                                                                                 # bagage and cargo handling equipment weight
W_fur = 55*N_fdc+32*N_pax+15*N_cc+K_lav*(N_pax)**1.33+K_buf*(N_pax)**1.12+109*(N_pax*((1+P_c)/100))**0.505+0.771*(MTOW/1000)  # furnishing weights
W_aux = 0.01*W_empty                                                                                                          # auxiliary gear weights
W_pt = 0.0045*MTOW                                                                                                            # weight of paint
W_fe = W_fc+W_hp+W_aie+W_els+W_api+W_ox+W_bc+W_fur+W_aux+W_pt                                                                 # total fixed equipment weight

##
##----- Output -----
##
# Wing weight
W_totros.append(W_w)
# Fuselage weight
W_totros.append(W_fus)
# Landing gear weight
W_totros.append(W_lg)
# Empennage weight
W_totros.append(W_emp)
# Power plant weight
W_totros.append(W_pp)
# Nacelle weight
W_totros.append(W_n)
# fixed equipment weight
W_totros.append(W_fe)
# total operational empty weight
totalweightros = sum(W_totros)
totalweightros = totalweightros/kglbs
#maximum take-off weight 
W_takeoffros = totalweightros+payload+fuel


##-------------------------------------------
##------------- Taking average --------------
##-------------------------------------------
#converting to kg

for i in range (0,len(W_tottor)):
    W_tottor[i] = W_tottor[i]/kglbs
for i in range (0,len(W_totros)):
    W_totros[i] = W_totros[i]/kglbs
                
#averaging
W_wing = (W_tottor[0] + W_totros[0])/2
W_fuselage = (W_tottor[1] + W_totros[1])/2
W_landinggear = (W_tottor[2] + W_totros[2])/2
W_empennage = (W_tottor[3] + W_totros[3])/2
W_propulsion = (W_tottor[4] + W_totros[4])/2
W_nacelle = (W_tottor[5] + W_totros[5])/2
W_equipment = (W_tottor[6] + W_tottor[7] + W_tottor[8] + W_tottor[9] + W_tottor[10] + W_tottor[11] + W_tottor[12] + W_totros[6])/2
OEW = (sum(W_totros)+sum(W_tottor))/2
MTOW = OEW + payload + fuel
#print
#print
#print 'Component weights for the average of the two methods:'
#print 'The wing weight =', W_wing, '[kg]'
#print 'The fuselage weight =', W_fuselage, '[kg]'
#print 'The landing gear weight =', W_landinggear, '[kg]'
#print 'The empennage weight =', W_empennage, '[kg]'
#print 'The propulsion weight =', W_propulsion, '[kg]'
#print 'The nacelle weight =', W_nacelle, '[kg]'
#print 'The equipment and furnishing weight =', W_equipment, '[kg]'
#print
#print 'The operational empty weight =', OEW, '[kg]'
#print 'The take-off weight =', MTOW, '[kg]'

string_class_II_final_version = ["W_wing","W_fuselage","W_landinggear","W_empennage","W_propulsion","W_nacelle","W_equipment","OEW","MTOW"]
