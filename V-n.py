__author__ = 'Menno vd Toorn'
from scipy.integrate import quad
from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from math import *
from parameters import *

#constants
n_max = 2.5
h = 12000
M = 0.79
R = 287.
a = 343

rho = 1.225
CL_max = 0.91 #change
WS = 5302
n_min = -1

rho_c = 1/515.378818 #convert kg/m3 to slug/ft3
l_c = 3.2808399 #convert meter to feet
WS_c = 0.020885 #convert N/m2 to lbf/ft2
v_c = 0.3048 #convert ft/s to m/s


V_C = M*a
V_D = V_C/0.7619
V_A = np.sqrt((2*n_max*WS)/(rho*CL_max))
V_H = np.sqrt((2*-n_min*WS)/(rho*CL_max))
V_S = np.sqrt((2*WS)/(rho*CL_max))
V1 = np.arange(0,V_A,1.)
V2 = np.arange(0,V_H,1.)
V3 = np.arange(V_A,V_D,1.)
V4 = np.arange(V_H,V_C,1.)
V5 = np.array([V_C,V_D])
q1 = 0.5*rho*V1*V1
q2 = 0.5*rho*V2*V2
n1 = q1*CL_max/WS
n2 = -q2*CL_max/WS
n3 = n_max*np.ones(len(V3))
n4 = n_min*np.ones(len(V4))
n5 = np.array([n_min,0])

V = np.arange(0,V_C,1.)
CL_a = 5.436 #change
MAC = 3.36 #change

h_f = h*l_c


Ub = 47
Uc = 33
Ud = 16

U = np.array([Ub,Uc,Ud])
g = 32.2
mu = (2*WS*WS_c)/(ISA(h_cr)[2]*rho_c*g*MAC*l_c*CL_a)
K = (0.88*mu)/(5.3+mu)
u = K*U*v_c



dn_c = (rho*V_C*CL_a*u[1])/(2*WS)
n_c = 1 + dn_c
n_f = 1 - dn_c

V_B = V_S*np.sqrt(n_c)

dn_d = (rho*V_D*CL_a*u[2])/(2*WS)
n_d = 1 + dn_d
n_e = 1 - dn_d


dn_b = (rho*V_B*CL_a*u[0])/(2*WS)
n_b = 1 + dn_b
n_g = 1 - dn_b


V6 = [0,V_B]
V7 = [V_B,V_C]
V8 = [V_C,V_D]

n6 = [1,n_b]
n7 = [n_b,n_c]
n8 = [n_c,n_d]
n9 = [1,n_g]
n10 = [n_g,n_f]
n11 = [n_f,n_e]

plt.plot(V1,n1,  color="blue", label='Maneuvering load')
plt.plot(V2,n2,  color="blue")
plt.plot(V3,n3,  color="blue")
plt.plot(V4,n4,  color="blue")
plt.plot(V5,n5,  color="blue")
plt.plot(V6,n6,  color="red", label = 'Gust load')
plt.plot(V7,n7, color="red")
plt.plot(V8,n8, color="red")
plt.plot(V6,n9,color="red")
plt.plot(V7,n10, color="red")
plt.plot(V8,n11, color="red")
plt.plot([V_D,V_D],[n_max,0],color="blue")
plt.legend(loc='upper left')

plt.ylabel("n")
plt.xlabel("V [m/s]")
plt.title("V-n diagram")
plt.show()

