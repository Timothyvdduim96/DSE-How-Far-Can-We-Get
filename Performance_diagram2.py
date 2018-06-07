import numpy as np
import matplotlib.pyplot as plt
from math import *
from liftdrag import C_D_cr, C_L_cr
from TWWS import thrust 
from isa import ISA_rho
'''
W_kg = 72564.                       #max to weight
S = 128.                            #wing surface
W_newton = W_kg * 9.80665

v = np.arange(1.,400.,1)
#rho = np.arange(0.38,1.225,0.0001)
rho = np.arange(1.225,0.38,-0.0001)

h30list = []
v30list = []
rholist = []

h20list = []
v20list = []

h10list = []
v10list = []

for i in v:
    for j in rho:
        RC = ((thrust * 1000. - (C_D_cr * 0.5 * j * i**2 * S )) * i)/W_newton  
        if 29.9 <= RC <= 30.1:
        #    rholist.append(round(j,5))
            h = ISA_rho(j)
            h30list.append(h)
            v30list.append(i)
        # elif 19.9 <= RC <= 20.1:
        #     h = ISA_rho(j)
        #     h20list.append(h)
        #     v20list.append(i)
        # elif 9.9 <= RC <= 10.1:
        #     h = ISA_rho(j)
        #     h10list.append(h)
        #     v10list.append(i)


# print hlist
# print vlist

#print rholist

#plt.plot(v10list,h10list, label = "10")
#plt.plot(v20list,h20list, label = "20")
plt.plot(v30list,h30list, label = "30")
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))

plt.show()

'''
'''
#USING FOR TEST
v = 193.314
rho = 1.225

RC = ((thrust * 1000. - (C_D_cr * 0.5 * rho * v**2 * S )) * sqrt((W_newton*2)/(S*rho*C_L_cr))/W_newton)
print RC
'''

print ISA_rho(0.68)