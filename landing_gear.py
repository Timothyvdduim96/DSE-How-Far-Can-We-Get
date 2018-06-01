# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 09:41:05 2018

@author: mrvan
"""

from scipy.integrate import quad
from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from math import *


g = 9.80665
MTOW = g*70000
Wland = g*60000

f = Wland/MTOW 

Nmw0 = f*MTOW/210000. #number of main gear wheels

Nmw = 4 * round(float(Nmw)/4) #round to nearest multiple of 4

Nnw = 2 #number of nose gear wheels

if Nmw <= 12:
    Nst = 2
else:
    Nst = 4
    
LCN = 1
p = 430*np.log(LCN)-680

Pmw = 0.92*MTOW/Nmw
Pnw = 0.08*MTOW/Nnw

#ln = 
#lm =
#psi = 
#z = 
#zt =
#ye =  
phi = 5. * (pi/180.)

#ymlg1 = (ln+lm)/(np.sqrt((ln*ln+np.tan(psi)*np.tan(psi))/(z*z)-1)) #lateral tip over criterion
#ymlg2 = b/2.-zt/np.tan(phi)
#ymlg3 = b/2.-ye/np.tan(phi)
#ymls = max([ymlg1,ymlg2,ymlg3])

print(phi)

