##Wing Layout
from math import *

#----------inputs--------
MTOW = 69177
#CLmax_clean
#CLmax_takoff
#CLmax_land

M_tf = 0.935 #technology factor for supercritical airfoils
M_cruise = 0.79
M_dd = M_cruise + 0.03

S = 128.
A = 14.

h = 10000. #m
p0 = 101325. #Pa
T0 = 288. #K
R = 287.
lambda_alt = -0.0065
g0 = 9.81
gamma = 1.4

#--------alt calc--------
p = p0 * (1-(lambda_alt*h)/T0)**(g0/(R*lambda_alt))
q = 0.5*gamma*p*M_cruise**2

#-------------outputs-----------
CL_cruise = MTOW/(q*S)


cos_lambdac_4 =  0.75 * (0.935/M_dd)
if M_cruise < 0.7:
    cos_lambdac_4 = 1

lambdac_4 = cos(cos_lambdac_4) #rad

lambda_w = 0.2*(2-lambdac_4)

lambdac_2 = atan(tan(lambdac_4) - 4/A * 0.25*(1-lambda_w)/(1+lambda_w)) #rad , from ADSEE II L1, slide31

lambdac_0 = atan(tan(lambdac_4) - 4/A * -0.25*(1-lambda_w)/(1+lambda_w))

b = sqrt(S*A)

c_r = (2*S)/((1+lambda_w)*b)

c_t = c_r * lambda_w

t_c = min(0.18, (cos(lambdac_2)**3*(M_tf-M_dd*cos(lambdac_2))-0.115*CL_cruise**1.5)/(cos(lambdac_2)**2))

dihedral = 1 - degrees(lambdac_4)/10

MAC = 0.75*c_r*(1+lambda_w+lambda_w**2)/(1+lambda_w)








