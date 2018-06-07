import numpy as np
import matplotlib.pyplot as plt
from math import *
from liftdrag import C_D_cr, C_L_cr
from TWWS import thrust 

W_kg = 72564.                       #max to weight
S = 128.                            #wing surface
W_newton = W_kg * 9.80665

v = np.arange(0,400,1)
rho = np.arange(0.4,1.225,0.0001)

for j in range(len(rho)):
    for i in range(len(v)):
        RC = (thrust - (C_D_cr * 0.5 * rho[j] * v[i]**2 * S )) * sqrt((W_newton*2)/(S*rho[j]*C_L_cr))
        if 0 <= RC <= 1:
            print rho