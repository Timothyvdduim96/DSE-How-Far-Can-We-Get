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
from isatool import atmos


Vh =  1
Vv = 0.100
Xcg_aft = 1
S = 
b =
MAC =
L_fus = 

Sh = Vh*S*MAC/(0.49*L_fus)
Sv = Vv*S*b/(0.45*L_fus)

sweep_h = 33
sweep_v = 40
Ah = 4.4
Av = 1.8
lambda_h = 0.5
lambda_v = 0.5

b_h = np.sqrt(A_h/S_h)
b_v = np.sqrt(A_v/S_v) #actual b_v = b_v/2

cr_h = 2*S_h/(b_h*(1+lambda_h))
ct_h = cr_h*lambda_h
cr_v = 2*S_v/(b_v*(1+lambda_v))
ct_v = cr_v*lambda_v

MAC_h = (2/3.)*(cr_h)*((1+lambda_h+lambda_h*lambda_h)/(1+lambda_h))
MAC_v = (2/3.)*(cr_v)*((1+lambda_v+lambda_v*lambda_v)/(1+lambda_v))

YMAC_h = (b_h/6.)*(1+2*lambda_h)/(1+lambda_h)
YMAC_v = (b_v/6.)*(1+2*lambda_v)/(1+lambda_v)

