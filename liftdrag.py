from math import *
from parameters import *
from TWWS import DPx,MTOW,S,C_D_0
import numpy as np
import matplotlib.pyplot as plt

#parameters
Afactor = 1.2    #factor increasing aspect ratio for winglets
WS = 0.98*DPx    #correct wing loading for fuel burn during cruise
sweep_LE = 0.68  #GET FROM WINGPLANFORM

#formulas

q = q(cruise_speed(h_cr),h_cr)
C_L_cr = MTOW*g/(q*S)
e = 0.85#4.61*(1-0.045*A**0.68)*(cos(sweep_LE))**0.15-3.1
K = 1/(pi*A*Afactor*e)
C_D_cr = C_D_0 + K*C_L_cr**2
LoverD = (q*C_D_0/WS+WS*K/q)**-1

CLlst = np.arange(0,C_L_cr,0.1)
CDlst = []
for i in range(len(CLlst)):
    CDlst.append(C_D_0 + K*CLlst[i]**2)

##plt.xlabel("C_D")
##plt.ylabel("C_L")
##plt.plot(CDlst,CLlst)
##plt.grid()
##plt.show()