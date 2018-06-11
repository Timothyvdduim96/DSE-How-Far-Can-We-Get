##Wing Layout
from math import *
from parameters import *

#----------inputs--------
#CLmax_clean
#CLmax_takoff
#CLmax_land

q = q(cruise_speed(value("h_cr")),value("h_cr"))

M_crit = 0.663 #NACA SC20612

C_L_cr = value("C_L_cr")#MTOW*g/(q*S)

M_tf = value("M_tf")

M_dd = value("M_cr") + 0.03

#--------alt calc--------
#p = p0 * (1-(lambda_alt*h)/T0)**(g0/(R*lambda_alt))
q = cruise_q(value("h_cr"))

#-------------outputs-----------
#CL_cruise = MTOW/(q*S)


cos_lambdac_4 =  0.75 * (M_tf/M_dd)

if value("M_cr") < 0.7:
    cos_lambdac_4 = 1

lambdac_4 = cos(cos_lambdac_4) #rad

taper = 0.2*(2-lambdac_4)

lambdac_2 = atan(tan(lambdac_4) - 4/value("A") * 0.25*(1-taper)/(1+taper)) #rad , from ADSEE II L1, slide31

lambdac_0 = atan(tan(lambdac_4) - 4/value("A") * -0.25*(1-taper)/(1+taper))

b = value("b")#sqrt(S*A)

c_r = value("c_r")#(2*S)/((1+taper)*b)

c_t = value("c_t")#c_r * taper

t_c = min(0.18, (cos(lambdac_2)**3*(M_tf-M_dd*cos(lambdac_2))-0.115*C_L_cr**1.5)/(cos(lambdac_2)**2))

dihedral = 1 - degrees(lambdac_4)/10

MAC = (2/3)*c_r*(1+taper+taper**2)/(1+taper)


string_wing_layout = ['lambdac_0','taper','b','c_r','c_t','t_c','dihedral','MAC','M_dd']







