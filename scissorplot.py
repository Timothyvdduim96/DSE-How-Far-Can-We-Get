from math import *
import matplotlib.pyplot as pyplot

#---------------------------------PARAMETERS---------------------------------------

S.M. = 0.05

#---------------------------------STABILITY----------------------------------------

m = (C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h/V)**2)**-1
q = -(x_bar_ac - S.M.)/(C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h/V)**2)

Sh_S_stab = m*x_bar_cg + q

#---------------------------------CONTROLLABILITY--------------------------------------

n = (C_L_h/C_L_Ah*l_h/c_bar*(V_h/V)**2)**-1
p = (C_m_ac/C_L_Ah-x_bar_ac)/(C_L_h/C_L_Ah*l_h/c_bar*(V_h/V)**2)

Sh_S_cont = n**x_bar_cg + p