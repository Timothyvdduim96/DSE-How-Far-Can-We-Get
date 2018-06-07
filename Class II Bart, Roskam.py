# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 11:30:11 2018

@author: Bart Jacobson
"""

#from parameters import *

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
kgmlbsgal = 0.00834540445 # kg/m3 to lbs/ US gal

''' Commercial transport aircraft Class II Weight estimation GD method, Roskam ''' 
Wtot = []

''' Inputs ''' 

# Wing inputs 

S = 128*(mft**2)            # wing surface area in ft2
Mh = 0.82                   # Maximum Mach number sea level
lt = 0.2687839065           # wing taper ratio
tc = 0.125                  # maximum wing thickness ratio t/c max
A = 14.                     # Wing aspect ratio
Wto = 69176.552 *kglbs      # take-off weight in lbs
nult = 1.5*2.5              # ultimate load factor
Lambda_half = 0.6297150096  # Wing semi - chord sweep angle

# Empennage inputs 
Sh = 1.                   # horizontal tail area in ft2
bh = 1.                   # horizontal tail span in ft
trh = 1.                  # horizontal tail maximum root thickness in ft
cmac = 1.                 # mean aerodynamic chord length
lh = 1.                   # Distance from wing quarter chord to hor. tail quarter chord in ft
zh = 1.                   # distance vertical tail root to horizontal tail
bv = 1.                   # vertical tail span in ft
Sv = 1.                   # Vertical tail area 
lv = 1.                   # Distance from wing quarter chord to vert. tail quarter chord in ft     
Sr = 1.                   # rudder area in ft2
Sv = 1.                   # Vertical tail surface area in ft2
Av = 1.                   # Vertical tail aspect ratio
lambdav = 1.              # Vertical tail taper ratio
Lambda_quarterv = 1.      # Vertical tail quarter chord sweep angle          

# Fuselage weight input 
Kinl = 1.                # correction factor for inlets not located on fuselage
qd = 1.                  # design dive dynamic pressure in psf
lf = 1.                  # fuselage length in feet
hf = 1.                  # fuselage height in feet      

# Nacelle weight inputs 
Ninl = 2.                # number of inlets
Ainl = 1.                # capture area per inlet in ft2
ln = 1.                  # nacelle length from inlet lip to compressor face in ft
P2 = 1.                  # maximum static pressure at engine compressor face in psi.   

# Landing gear inputs
# based on Wto

# Engine Weight inputs

neng = 2.               # number of engines
Weng = 6250.          # afgelezen uit roskam fig 6.1 for thrust of 181000 N for two engines, gives engine weight of 6250 lbs per engine

# Fuel system inputs

Nt = 8.                 # number of separate fuel tanks
Wf = 9530. *kglbs                 # mission fuel weight (including reserves) in lbs
Kfsp = 810. * kgmlbsgal             # density in lbs/gal

# propusion system inputs

b = 42.3 * mft              # wingspan



''' Equations ''' 
# Wing weight
Ww = (0.00428*(S**0.48)*(A)*(Mh**0.43)*((Wto*nult)**0.84)*(lt**0.14))/((100*(tc))**0.76 * (sp.cos(Lambda_half))**1.54)

#Empennage weight 
#horizontal tail
Wh = 0.0034 * (((Wto*nult)**0.813)*(Sh**0.584)*((bh/trh)**0.033)*((cmac/lh)**0.28))**0.915
# Vertical tail
Wv = 0.19 * (((1 + (zh/bv))**0.5)*((Wto*nult)**0.363)*(Sv**1.089)*(Mh**0.601)*(lv**-0.726)*((1 + (Sr/Sv))**0.217)*(Av**0.337)*((1+lambdav)**0.363)*((sp.cos(Lambda_quarterv))**-0.484))**1.014
Wemptot = Wh + Wv

# Fuselage Weight 
Wf = 10.43 * (Kinl**1.42) * ((qd/100)**0.283) * ((Wto/1000)**0.95) * ((lf/hf)**0.71)

# Nacelle weight (includes air induction system)

Wn = 3.0 * (Ninl) * ((Ainl**0.5) * ln * (P2))**0.731

# Landing gear weight 

Wlg = 62.21 * ((Wto/1000.)**0.84)

# Engine weight total 

We = neng*Weng      

# Fuel system

Wfs = 80. * (neng + Nt - 1 ) + 15. * (Nt**0.5) * ((Wf/Kfsp)**0.333)

# Propulsion system
# engine controls
Wec = 88.46 * (((lf + b)* neng)/100)**0.294
# engine starting system
Wess = 38.93 * (We/1000.)**0.918

Wprop = Wec + Wess


''' Outputs ''' 
# Wing section weight
print 'Weight wing section, Ros =', Ww/kglbs ,'[kg]'
Wtot.append(Ww)

# Empennage weight
print 'Weight empennage section, Ros =', Wemptot/kglbs ,'[kg]'
Wtot.append(Wemptot)

# Fuselage weight
print 'Weight fuselage section, Ros =', Wf/kglbs ,'[kg]'
Wtot.append(Wf)

# Nacelle weight
print 'Weight Nacelle section, Ros =', Wn/kglbs ,'[kg]'
Wtot.append(Wn)

# Landing gear weight
print 'Weight Landing gear section, Ros =', Wlg/kglbs ,'[kg]'
Wtot.append(Wlg)

# Engine weight
print 'Weight engine section, Ros =', We/kglbs ,'[kg]'
Wtot.append(We)

# Fuel system weight
print 'Weight fuel system section, Ros =', Wfs/kglbs ,'[kg]'
Wtot.append(Wfs)



# Propulsion weight
print 'Weight propulsion section, Ros =', Wprop/kglbs ,'[kg]'
Wtot.append(Wprop)





























print 'Weight Total, Ros =', sum(Wtot)/kglbs ,'[kg]', len(Wtot)
