# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:45:40 2018

@author: emad

Aircraft Performance Program
"""

import numpy as np
import matplotlib.pyplot as plt
from math import *
from liftdrag import C_D_cr
from TWWS import thrust, C_L_maxto

#----------------------------------------------
W_kg = 72564                       #max to weight
S = 127.95                      #wing surface
rho = 1.225
#---------------------------------------------

W_newton = W_kg * 9.80665
V_stall = sqrt((W_newton/S)*(2/rho)*(1/C_L_maxto))

v = np.arange(V_stall,70,1)


Pa_list = []
for i in v:
    Pa = thrust * v
    Pa_list.append(Pa)

print v