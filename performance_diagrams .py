# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:45:40 2018

@author: emad

Aircraft Performance Program
"""
'''

#------------FOR VERIFICATION ONLY-----------------------------

import numpy as np
import matplotlib.pyplot as plt
from math import *
# from liftdrag import C_D_cr, C_L_cr
#from TWWS import thrust 

#----------------------------------------------
W_kg = 72564.                       #max to weight
S = 18.58                      #wing surface
#rho = [0.002377, 1.12102, 1.02393, 0.933405, 0.849137, 0.770816, 0.698145]
#---------------------------------------------
rho = 1.225
C_D_cr = 0.0239
C_L_cr = 0.280

W_newton = 4535.92 * 9.81 #W_kg * 9.80665
thrust = 907.18 * 9.81
#V_stall = sqrt((W_newton/S)*(2/rho[0])*(1/C_L_cr))


v = 78.33 #np.arange(50,200,1)   
#v = np.arange(V_stall,335,1)
Drag_list = []
Pa_list = []
Pr_list = []
PaPrlist = []

#a new list for each density???

#for j in range(len(rho)):
#for i in range(len(v)):
Pa = thrust * v 
Pa_list.append(Pa)
D = C_D_cr * 0.5 * rho * v**2 * S
Pr = D * v
Pr_list.append(Pr)
PaPrlist.append(((Pa - Pr)/W_newton))
    #
    #plt.plot(v,Pa_list)
    #plt.plot(v,Pr_list)
    #plt.show()
    
print PaPrlist

# plt.plot(v,PaPrlist[:214])
# plt.show()
'''

#--------------ACTUAL CODE------------------------

import numpy as np
import matplotlib.pyplot as plt
from math import *
from liftdrag import C_D_cr, C_L_cr
from TWWS import thrust, C_D_0
#----------------------------------------------
W_kg = 72564.                       #max to weight
S = 128.                      #wing surface
rho = 1.225#, 1.12102, 1.02393, 0.933405, 0.849137, 0.770816, 0.698145]
#thrust = 130
#---------------------------------------------
W_newton = W_kg * 9.80665

V_stall = sqrt((W_newton/S)*(2/rho)*(1/C_L_cr))

v = np.arange(V_stall,360.,1.)
vnorm = np.arange(0,360,1)

Pa_list = []
Pr_list = []
PaPrlist = []

for k in range(len(vnorm)):
    Pa = thrust * vnorm[k] * 1000
    Pa_list.append(Pa)    

# for j in range(len(rho)):
for i in range(len(v)):
    #Pa = thrust * v[i] * 1000
    #Pa_list.append(Pa)
    D = C_D_cr * 0.5 * rho * v[i]**2 * S
    #D = (C_D_0 * 0.5 * rho *v[i]**2 * S) + ((4*W_newton**2)/(pi*14*0.8*rho*v[i]**2 *S))
    Pr = D * v[i]
    Pr_list.append(Pr)
    #Pnew = (Pa - Pr)/W_newton
    #PaPrlist.append(Pnew)
    
for b in range(len(Pr_list)):
    Pnew = (Pa_list[121 + b] - Pr_list[b])/W_newton
    PaPrlist.append(Pnew)
    

plt.plot(vnorm,Pa_list)
plt.plot(v,Pr_list)
plt.show()
    

plt.plot(v,PaPrlist)
plt.show()
# plt.plot(v,PaPrlist[215:429])

# print thrust
# print C_L_cr
# print C_D_cr

# print len(Pa_list)
# print len(Pr_list)
