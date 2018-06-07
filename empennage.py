# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:47:29 2018

@author: mrvan
"""

__author__ = 'Menno vd Toorn'
from scipy.integrate import quad
from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from math import *




Vh =  1         #horizontal tail volume
Vv = 0.100      #vertical tail volume

S = 128            #wing surface area
b = 42.33202098             #wing span
MAC =  3.778287263         #mean aerodynamic chord
L_fus = 46.55        #fuselage length

lh = 27.787         #horizontal tail arm [m]
lv = 0.45*L_fus
Sh = Vh*S*MAC/(lh)   #horizontal tail surface area
Sv = Vv*S*b/(lv)     #vertical tail surface area

sweep_h = 33    
sweep_v = 40
Ah = 4.4    #aspect ratio
Av = 1.8
lambda_h = 0.5  #taper
lambda_v = 0.5

b_h = np.sqrt(Ah*Sh)  #horizontal tail span
b_v = np.sqrt(Av*Sv) #actual b_v = b_v/2

cr_h = 2*Sh/(b_h*(1+lambda_h))
ct_h = cr_h*lambda_h
cr_v = 2*Sv/(b_v*(1+lambda_v))
ct_v = cr_v*lambda_v

MAC_h = (2/3.)*(cr_h)*((1+lambda_h+lambda_h*lambda_h)/(1+lambda_h))
MAC_v = (2/3.)*(cr_v)*((1+lambda_v+lambda_v*lambda_v)/(1+lambda_v))

YMAC_h = (b_h/6.)*(1+2*lambda_h)/(1+lambda_h) 
YMAC_v = (b_v/6.)*(1+2*lambda_v)/(1+lambda_v)

##print (cr_h)
##print (ct_h)
##print (Sh)
##print (b_h)
##print (MAC_h)
##print (YMAC_h)
