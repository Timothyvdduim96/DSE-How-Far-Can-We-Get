# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:46:12 2018

@author: Bart Jacobson
"""

#from parameters import *
#from TWWS import S

import numpy as np
import scipy as sp
import math


# conversions 
mskts =  1.94384449           #m/s to knots 
kglbs = 2.20462262  #kg to pounds
mft = 3.2808399     #meter to feet
kmnm = 0.539956803  #km to nautical mile
degrad= (1./180.)*sp.pi # degrees to rad
newlbs = 0.224808943 # newton to lbs thrust

''' inputs are 14 weight groups''' 

Wtot = []  # list for summation of section weights into total weight

''' input 1 --- Wing group --- '''

#   Variables wing geometry, length in feet weight in pounds!
kwg = 0.0017    
Wzf = 59646.8746*kglbs # aircraft zero fuel weight
nult= 1.5*2.5   # ultimate load factor = 1.5 times limit load
trmax = 0.65*mft # wing root maximum thickness
b = 42.3 *mft         # wingspan
S = 128*(mft**2)      # Wing surface area
Lambda_half = 0.6297150096 # wing sweep half chord in radians

# function Weight wing group

Wwg1 = kwg*(Wzf**0.7)*(S**0.3)*(nult**0.55)*(trmax**-0.3)*((b/sp.cos(Lambda_half))**1.05)*(1+sp.sqrt((6.25*sp.cos(Lambda_half))/b))

Wwg = 0.95*Wwg1  #correction for wing mounted engines


print 'Weight wing group =', Wwg/kglbs ,'[kg]'
Wtot.append(Wwg)

''' input 2 --- Fuselage group ---'''

#Variables fuselage, Check lengths in feet, weight in pounds!
dfus = 2*1.904 *mft #diameter fuselage
lfus = 42.918 * mft # length fuselage
Fnc = 1.5 # fineness ratio nose cone
Ftc = 2.5 # fineness ratio tail cone 
F = lfus/dfus # fineness ratio fuselage

#function for surface area fuselage
Sg = sp.pi*dfus*lfus*(1-(Fnc/(3*F))-(Ftc/(2*F)))    #Surface area of fuselage, gross shell area

# weight fuselage calculation

kfus = 0.0227
Vd = 355.6503 *mskts #Dive speed in knots equivalent airspeed
#lh = 25. *mft # wing root quarter chord to tail root quarter chord
#bfus = 3.*mft # maximum width
#hfus = 3.*mft # maximum height

Wfus1 = kfus*(Sg**1.2)*sp.sqrt(Vd*(F/4))

Wfus = Wfus1 * 1.07 # Torenbeek 7 percent correction factor

print 'Weight fuselage group =', Wfus/kglbs ,'[kg]'
Wtot.append(Wfus)

''' input 3 --- Landing gear group ---'''

#input parameters landing gear
Wg = 43611.43 *kglbs #gross weight (MTOW)

# Weight main gear
Wmg = 40. + 0.16*Wg**(3./4.)+ 0.019*Wg + 1.5*10**(-5.)*Wg**(3./2.) 

# Weight nose gear
Wng = 20. + 0.10*Wg**(3./4.)+ 2.*10**(-6)*Wg**(3./2.)

Wlg = Wmg + Wng + 300.* kglbs # mass total gear plus 300 kg for EGTS

print 'Weight Landing gear group =', Wlg/kglbs ,'[kg]'
Wtot.append(Wlg)


''' input 4 --- Tail group ---'''

#input parameters Tail group
kh = 1.1       #account for different tail configurations
Sh = 31. *(mft**2)       #horizontal tail surface

hh = 6.26 *mft       # height horizontal tail above fuselage centerline
bv = 6.26 *mft       # height of the tip of the vertical tail above the fuselage centerline
Sv = 21.5 *(mft**2)  # vertical tail surface

kv = 1. + 0.15 * ((Sh*hh)/(Sv*bv))   


# Vd is dive speed [kts], determined in fuselage section

Lambda_h = (29./180.)*sp.pi     #sweep horizontal tail
Lambda_v = (34./180.)*sp.pi     #sweep vertical tail
# fuction tail group weight

Wth = kh*Sh*(2.+4.15*math.erf((((Sh**0.2)*Vd)/((10**3)*sp.sqrt(sp.cos(Lambda_h)))) -0.65))  #horizontal tail weight

Wtv = kv*Sv*(2.+4.15*math.erf((((Sv**0.2)*Vd)/((10**3)*sp.sqrt(sp.cos(Lambda_v)))) -0.65))  #vertical tail weight

Wt = Wth + Wtv #total tail weight

print 'Weight tail group =', Wt/kglbs ,'[kg]'
Wtot.append(Wt)

''' input 5 --- Propulsion group ---'''

#input parameters engine group
# 177 kN - 220 kN

Fto = (220000./2.)*newlbs   #Takeoff static thrust per engine
ne = 2.           #number of engines

We = 2.7 * Fto**0.75    #Engine weight of one engine

Wpg = 10*(ne*We)**0.8       #weight propulsion group

print 'Weight Propulsion group =', Wpg/kglbs ,'[kg]'
Wtot.append(Wpg)

''' input 6 --- Nacelle group ---'''

# input parameters nacelle group
# see inputs engine weight
# mass nacelle group

Wng = 4.5*(ne*We)**0.9 - Wpg 

print 'Weight Nacelle group =', Wng/kglbs ,'[kg]'
Wtot.append(Wng)

''' input 7 --- Flight controls group ---'''

Wfc = 1.44 * Wg**0.625

print 'Weight Flight controls group =', Wfc/kglbs ,'[kg]'
Wtot.append(Wfc)

''' input 8 --- Auxiliary power unit group ---'''

# APU will not be used in our design

#'''-------------------------------------------------'''
#''' Total mass so far'''
#
#Wtot = [Wwg, Wfus, Wlg, Wt, Wpg, Wng, Wfc]

#Wtot = sp.sum(Wtot)
#
#print 'Weight total =', Wtot ,'[lbs]'

''' input 9 --- Instrument group ---'''

Wig = 0.55*Wg**0.6

print 'Weight Instrument group =', Wig/kglbs ,'[kg]'
Wtot.append(Wig)

''' input 10 --- Hydraulic and pneumatic group ---'''

Whp = 0.1*Wg**0.8

print 'Weight Hydraulic and pneumatic group =', Whp/kglbs ,'[kg]'
Wtot.append(Whp)

''' input 11 --- Electrics group ---'''

Wbat = 25.5 *kglbs  #mass of additional batteries due to APU removal

Wel = 9 * Wg**0.473 + Wbat

print 'Weight Electronics group =', Wel/kglbs ,'[kg]'
Wtot.append(Wel)


''' input 12 --- Avionics group ---'''

#Wav = 0.09*Wg**0.8 use as check
Wempty= 38369.815 *kglbs # OEW
R = 6254 * kmnm # Ferry range


Wav = 0.575*Wempty**0.55 * R**0.25

print 'Weight Avionics group =', Wav/kglbs ,'[kg]'
Wtot.append(Wav)


''' input 13 --- Equipment and furnishing group ---'''

Wef = 0.211 *Wzf**0.91

print 'Weight Equipment and furnishing group =', Wef/kglbs ,'[kg]'
Wtot.append(Wef)



''' input 14 --- Air conditioning and anti-icing group ---'''


Waci = 5 * sp.sqrt(Wg)

print 'Weight Air conditioning and anti-icing group =', Waci/kglbs ,'[kg]'
Wtot.append(Waci)







print 'Total weight', np.sum(Wtot) ,'[lbs]'
print 'Total weight', np.sum(Wtot)/kglbs ,'[kg]'

print len(Wtot)
