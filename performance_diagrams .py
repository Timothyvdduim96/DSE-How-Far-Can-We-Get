# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:45:40 2018

@author: emad

Aircraft Performance Program
"""

import numpy as np
import matplotlib.pyplot as plt
from math import *
from liftdrag import C_D_cr, C_L_cr
from TWWS import thrust 

#----------------------------------------------
W_kg = 72564                       #max to weight
S = 127.95                      #wing surface
rho = [1.225, 1.12102, 1.02393, 0.933405, 0.849137, 0.770816, 0.698145]
#---------------------------------------------


W_newton = W_kg * 9.80665

V_stall = sqrt((W_newton/S)*(2/rho[0])*(1/C_L_cr))
    
v = np.arange(V_stall,335,1)
Drag_list = []
Pa_list = []
Pr_list = []
PaPrlist = []

#a new list for each density???

for j in range(len(rho)):
    for i in range(len(v)):
        Pa = thrust * v[i] * 1000
        Pa_list.append(Pa)
        D = C_D_cr * 0.5 * rho[j] * v[i]**2 * S
        Pr = D * v[i]
        Pr_list.append(Pr)
        PaPrlist.append(((Pa - Pr)/W_newton))
    #
    #plt.plot(v,Pa_list)
    #plt.plot(v,Pr_list)
    #plt.show()
    
    plt.plot(v,PaPrlist)
    plt.show()