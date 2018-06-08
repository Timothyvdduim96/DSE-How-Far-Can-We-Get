#####LIFT Calculation + Shear and Moment Diagram of Fuselage (Side view)

from math import *
from parameters import *


#Input
C_m_w=+0.25 
h_TO=0 
MAC=3.36
T=10000 #Thrust N
z_EW=1
n=2.5*1.5
MTOW=70000 #kg
alpha_TO=deg_to_rad*5
gamma_TO=deg_to_rad*12
x_cg_TO=12.5
x_ac_w=12.0
l_h=20.947
Sh=17.4
V_rot=110 #m/s


#Selected Variables
V=V_rot
W=MTOW
x_cg=x_cg_TO


#---------Lift Calculation------------#

def Lift_wings(M_w,T,z_EW,n,W,x_cg,x_ac_w,l_h,alpha,theta):
    L_t=(M_w+T*z_EW+n*W*cos(theta)*g*(x_cg-x_ac_w))/(l_h*cos(alpha))
    L_w=(n*W*cos(theta))/(cos(alpha))-L_t
    
    return L_w,L_t


#Output -----Lift Calculation of Wing and Tail
theta_TO=alpha_TO+gamma_TO #Pitch angle [rad]
M_w=0.5*q(V,h_TO)*Sh*MAC*C_m_w
L_w,L_t=Lift_wings(M_w,T,z_EW,n,W,x_cg,x_ac_w,l_h,alpha_TO,theta_TO)

print L_w,"Wing Force"
print L_t,"Tail Force"

