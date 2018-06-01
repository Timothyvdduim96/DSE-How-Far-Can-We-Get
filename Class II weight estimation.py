##--------------------------------------
##import libraries
##--------------------------------------
import numpy as np
import scipy as sp
import math

##--------------------------------------
##converstion factors
##--------------------------------------
mft     = 3.2808399        # conversion factor meters to feet
kglbs   = 2.20462262       # conversion factor kilograms to pounds
sqmsqft = 10.7639104       # conversion factor square meters to square feet
mskts   = 1.94384449       # conversion factor meters per seconds to knots
degrad  = 0.0174532925     # conversion factor degrees to radians
kmnm    = 0.539956803      # conversion factor kilometers to nautical miles
Nlbs    = 0.224808943      # conversion factor newtons to pounds
##--------------------------------------
##Class I weight estimation
##--------------------------------------


##--------------------------------------
##Class II weight estimation
##--------------------------------------
'''!!!!!all weights should be in pounds!!!!!'''
'''!!!!!all lengths should be in meters!!!!!'''
W_tot = []   #empty list for all weight groups


## ----- Wing group -----
#inputs
k_wg        = 0.0021            #constant
W_zf        = 59646.8746*kglbs  #zero fuel weight [lbs]
S           = 128.*sqmsqft      #wing surface area [sqft]
n_ult       = 1.5*2.5           #ultimate load factor
t_rm        = 0.65*mft          #wing root maximum thickness (for B737) [ft]
b           = 42.3*mft          #wingspan [ft]
lambda_half = 0.6297150096      #half chord sweep angle [rad]

#equations
W_wg = k_wg*(W_zf)**0.7*(S)**0.3*(n_ult)**0.55*(t_rm)**-0.3*(b/np.cos(lambda_half))**1.05*(1+np.sqrt((6.25*np.cos(lambda_half))/b))   #fuselage group weight
W_wg = W_wg*0.95    #correction for wing mounted engines

#output
print 'Wing group weight =', W_wg/kglbs, '[kg]'
W_tot.append(W_wg)


##----- Fuselage group -----
#inputs
pi      = np.pi            #pi
d_fus   = 1.904*2*mft      #fuselage diameter
l_fus   = 42.918*mft       #fuselage length
F_NC    = 1.5              #fineness ratio nosecone
F_TC    = 2.5              #fineness ratio tailcone
k_fus   = 0.032            #constant
V_D     = 355.6503*mskts   #dive speed [kts]
#equations
F = l_fus/d_fus                                      #fuselage fineness ratio
S_g = pi*d_fus*l_fus*(1-(F_NC/(3*F))-(F_TC/(2*F)))   #gross wetted area
W_fus = k_fus*(S_g)**1.2*np.sqrt(V_D*(F/4))          #fuselage group weight
W_fus = W_fus*1.07                                   #correction for pressurized cabin

#output
print 'Fuselage group weight =', W_fus/kglbs, '[kg]'
W_tot.append(W_fus)


##-----Landing gear group-----
#inputs
W_g = 69176.552*kglbs     #MTOW

#equations
W_MG = 40.+0.16*W_g**0.75+0.019*W_g+1.5*10**-5*W_g**1.5  #main landing gear weight
W_NG = 20.+0.10*W_g**0.75+2*10**-6*W_g**1.5             #nose gear weight
W_LG = W_MG+W_NG+300*kglbs                            #total landing gear weight + EGTS system

#output
print 'Landing gear group weight =', W_LG/kglbs, '[kg]'
W_tot.append(W_LG)


##----- Tail group -----
#inputs
k_h      = 1.1              #constant horizontal tail
S_h      = 31.0*sqmsqft     #horizontal tail surface
S_v      = 21.50*sqmsqft    #vertical tail surface
lambda_h = 29.0*degrad      #horizontal tail sweep
lambda_v = 34.0*degrad      #vertical tail sweep
h_h      = 6.26*mft         #height of horizontal tail surface above fuselage centerline
b_v      = 6.26*mft         #height of vertical tail surface above fuselage centerline

#equations
k_v = 1+0.15*((S_h*h_h)/(S_v*b_v))   #constant vertical tail
W_ht = k_h*S_h*(2.+4.15*math.erf((((S_h)**0.2*V_D)/((10)**3*np.sqrt(np.cos(lambda_h))))-0.65))   #horizontal tail weight
W_vt = k_v*S_v*(2.+4.15*math.erf((((S_v)**0.2*V_D)/((10)**3*np.sqrt(np.cos(lambda_v))))-0.65))   #vertical tail weight
W_t = W_ht+W_vt #total tail weight

#output
print 'Tail group weight =', W_t/kglbs, '[kg]'
W_tot.append(W_t)


##----- Propulsion group -----
#inputs
F_to = (181./2)*(10)**3*Nlbs     #take-off static thrust per engine [lbs]
n_e  = 2.                        #number of engines

#equations
W_e = 2.7*(F_to)**0.75      #engine weight for one engine
W_pg = 10.*(n_e*W_e)**0.8   #propulsion goup weight
wpgtor = 1.18*1.15*n_e*W_e
print wpgtor
#output
print 'propulsion group weight =', W_pg/kglbs, '[kg]'
W_tot.append(W_pg)


##----- Nacelle group -----
#equations
W_ng = 4.5*(n_e*W_e)**0.9-W_pg #nacelle group weight

#output
print 'nacelle group weight =', W_ng/kglbs, '[kg]'
W_tot.append(W_ng)


##----- Flight controls group -----
#equations
W_fc = 1.44*(W_g)**0.625   #flight controls group weight

#output
print 'flight controls group weight =', W_fc/kglbs, '[kg]'
W_tot.append(W_fc)


##----- APU group -----
#APU is not present in our aircraft


##----- Instruments group -----
#equations
W_ig = 0.55*(W_g)**0.6   #instruments group weight

#output
print 'instruments group weight =', W_ig/kglbs, '[kg]'
W_tot.append(W_ig)


##----- Hydraulic and pneumatic group -----
#equations
W_hp = 0.1*(W_g)**0.8   #hydraulic and pneumatic group weight

#output
print 'hydraulic and pneumatic group weight =', W_hp/kglbs, '[kg]'
W_tot.append(W_hp)


##----- Electrical group -----
#equations
W_el = 9*(W_g)**0.473+25.5*kglbs #electrical group weight + extra battery unit

#output
print 'electrical group weight =', W_el/kglbs, '[kg]'
W_tot.append(W_el)


##----- Avionics group -----
#inputs
W_empty = 38369.815*kglbs    #empty weight
R = 6254*kmnm                #maximum range/ferry range

#equations
W_av = 0.575*(W_empty)**0.55*(R)**0.25   #avionics group weight

#output
print 'avionics group weight =', W_av/kglbs, '[kg]'
W_tot.append(W_av)


#----- equipment and furnishing group -----
#equations
W_ef = 0.211*(W_zf)**0.91   #equipment and furnishing group weight

#output
print 'equipment and furnishing group weight =', W_ef/kglbs, '[kg]'
W_tot.append(W_ef)


#----- air conditioning and anti-icing group -----
#inputs

#equations
W_aci = 5*np.sqrt(W_g)

#output
print 'air conditioning and anti-icing group weight =', W_aci/kglbs, '[kg]'
W_tot.append(W_aci)
 

##--------------------------------------
##total weight
##--------------------------------------
totalweightlbs = sum(W_tot)
print
print
print 'the operation empty weight =', totalweightlbs, '[lbs]'
totalweightkg = totalweightlbs/kglbs
print 'the operation empty weight =', totalweightkg, '[kg]'

