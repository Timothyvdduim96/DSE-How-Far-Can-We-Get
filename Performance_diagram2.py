import numpy as np
import matplotlib.pyplot as plt
from math import *
from liftdrag import C_D_cr, C_L_cr
from TWWS import thrust 
from isa import ISA_rho

W_kg = 72564.                       #max to weight
S = 128.                            #wing surface
W_newton = W_kg * 9.80665

v = np.arange(1.,400.,1.)
rho = np.arange(1.225,0.1,-0.0001)

hlist = []
vlist = []
rholist = []

for i in v:
    for j in rho:
        RC = ((thrust * 1000. - (C_D_cr * 0.5 * j * i**2 * S )) * i)/W_newton  
        if 29.9 <= RC <= 30.1:
            #rholist.append(round(j,5))
            h = ISA_rho(j)
            hlist.append(h)
            vlist.append(i)

# print hlist
# print vlist

print rholist
# plt.plot(vlist,hlist)
plt.show()


'''
#USING FOR TEST
v = 193.314
rho = 1.225

RC = ((thrust * 1000. - (C_D_cr * 0.5 * rho * v**2 * S )) * sqrt((W_newton*2)/(S*rho*C_L_cr))/W_newton)
print RC
'''
