##Wing Layout
from math import *
from TWWS import S,MTOW
from parameters import *

#----------inputs--------
#CLmax_clean
#CLmax_takoff
#CLmax_land

<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> af6e807275de47b92cbeaf27f70ca0418002ab59
q = q(cruise_speed(h_cr),h_cr)

C_L_cr = MTOW*g/(q*S)

<<<<<<< HEAD
>>>>>>> ea395c35dc7b2e8e271abc3cbabb458ff85c7378
=======
>>>>>>> af6e807275de47b92cbeaf27f70ca0418002ab59
M_dd = M_cr + 0.03

#--------alt calc--------
#p = p0 * (1-(lambda_alt*h)/T0)**(g0/(R*lambda_alt))
q = cruise_q(h_cr)

#-------------outputs-----------
#CL_cruise = MTOW/(q*S)


cos_lambdac_4 =  0.75 * (M_tf/M_dd)

if M_cr < 0.7:
    cos_lambdac_4 = 1

lambdac_4 = cos(cos_lambdac_4) #rad

taper = 0.2*(2-lambdac_4)

lambdac_2 = atan(tan(lambdac_4) - 4/A * 0.25*(1-taper)/(1+taper)) #rad , from ADSEE II L1, slide31

lambdac_0 = atan(tan(lambdac_4) - 4/A * -0.25*(1-taper)/(1+taper))

b = sqrt(S*A)

c_r = (2*S)/((1+taper)*b)

c_t = c_r * taper

t_c = min(0.18, (cos(lambdac_2)**3*(M_tf-M_dd*cos(lambdac_2))-0.115*C_L_cr**1.5)/(cos(lambdac_2)**2))

dihedral = 1 - degrees(lambdac_4)/10

MAC = (2/3)*c_r*(1+taper+taper**2)/(1+taper)


string_wing_layout('lambdac_4 ','lambdac_2','lambdac_0','taper','b','c_r','c_t','t_c','dihedral','MAC','M_dd')







