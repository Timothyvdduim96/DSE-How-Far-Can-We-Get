#####LIFT Calculation + Shear and Moment Diagram of Fuselage (Side view)

from math import *
from parameters import *


#Input
C_m_w=+0.25 
h_TO=0 
MAC=2.5
T=10000 #Thrust N
z_EW=1
n=2.5*1.5
W=70000 #kg
alpha_TO=deg_to_rad*5
gamma_TO=deg_to_rad*12
x_cg=12.5
x_ac_w=12.0
l_h=25.0
S_w=15
V_TO=80 #m/s


#---------Lift Calculation------------#

def Lift_wings(M_w,T,z_EW,n,W,x_cg,x_ac_w,l_h,alpha,theta):
    L_t=(M_w+T*z_EW+n*W*cos(theta)*g*(x_cg-x_ac_w))/(l_h*cos(alpha))
    L_w=(n*W*cos(theta))/(cos(alpha))-L_t
    
    return L_w,L_t


#Output -----Lift Calculation of Wing and Tail
theta_TO=alpha_TO+gamma_TO #Pitch angle [rad]
M_w=0.5*q(V_TO,h_TO)*S_w*MAC*C_m_w
L_w,L_t=Lift_wings(M_w,T,z_EW,n,W,x_cg,x_ac_w,l_h,alpha_TO,theta_TO)


#######Shear Diagram Side View###############
W_eng=1
W_emp=1
W_wing=1
W_fuel=1
L_fus=42

def Shear_fuction_side_view(x,W,W_eng,W_emp,W_fuel,W_wing,x_cg_eng,x_ac_wing,L_w,L_t,l_h,x_cg_wing,x_cg_emp,alpha_angle,gamma_angle)
    x_ac_tailwing=l_h+x_ac_wing    
    theta_angle=gamma_angle+alpha_angle    
    W_rest=W-W_eng-W_wing-W_fuel-W_emp
    w_rest=W_rest/float(L_fus)
    
    if 0<x<x_cg_eng:
        V=-w_rest*x
    elif x_cg_eng<x<x_cg_wing:
        V=-w_rest*x*cos(theta_angle)+L_w*cos(alpha_angle)
        



