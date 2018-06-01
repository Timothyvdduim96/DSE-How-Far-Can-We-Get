from math import *
from TWWS import A, DPx, MTOW, S, designdata,ch, C_D_0, C_Lland
import numpy as np
import matplotlib.pyplot as plt

cfelst = [0.0045,0.0048]

#fixed
M = 0.79
gamma = 1.4
R = 287.05
T0 = [288.15,216.65]
rho0 = [1.225,0.3639]
ag = 0.0065
Afactor = 1.2 #factor increasing aspect ratio for winglets
WS = 0.98*DPx
g = 9.80665
h = 12000

if h > 11000:
    T = T0[1]
    rho = rho0[1]*e**(-g/(R*T)*(h-11000))
else:
    T = T0[0]-ag*h
    rho = rho0[0]*(T/T0[0])**(-g/(-ag*R)-1)
    
a = sqrt(gamma*R*T)
V = M*a

#variables
material = eval(designdata[18][ch]) #1 = composite, 2 = metal
C_f_e = cfelst[material-1]
SwetSref = 5.5#eval(designdata[19][ch])/S
C_L = MTOW*g/(0.5*rho*V**2*S)
q = 0.5*rho*V**2
e = 0.85#1.78*(1-0.045*A**0.68)-0.64
#C_D_0 = 0.1C_f_e*SwetSref
K = 1/(pi*A*Afactor*e)
C_D = C_D_0 + K*C_L**2
LoverD = (q*C_D_0/WS+WS*K/q)**-1

print "C_L_cruise = ", C_L
print "L/D = ", LoverD
print "C_D_cruise = ", round(C_D,4)
print "C_D_0 = ", round(C_D_0,4)

CLlst = np.arange(-2,C_Lland,0.1)
CDlst = []
for i in range(len(CLlst)):
    CDlst.append(C_D_0 + K*CLlst[i]**2)

plt.xlabel("C_L")
plt.ylabel("C_D")
plt.plot(CLlst,CDlst)
plt.grid()
plt.show()
