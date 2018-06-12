from math import *
from parameters import *
import numpy as np
import matplotlib.pyplot as plt

#parameters
Afactor = value("Afactor")    #factor increasing aspect ratio for winglets
WS = 0.98*value("WS")    #correct wing loading for fuel burn during cruise
sweep_LE = value("lambdac")  #GET FROM WINGPLANFORM

#--------------------------
#This is for the performance diagrams

q3 = q(cruise_speed(value("h_cr")),914.1)
q6 = q(cruise_speed(value("h_cr")),1828.8)
q9 = q(cruise_speed(value("h_cr")),2743.2)
q12 = q(cruise_speed(value("h_cr")),3657.6)
q15 = q(cruise_speed(value("h_cr")),4572)
q18 = q(cruise_speed(value("h_cr")),5486.4)


#-------------------------
#formulas

q = q(cruise_speed(value("h_cr")),value("h_cr"))
C_L_cr = value("MTOW")*g/(q*value("S"))
e = value("e")#4.61*(1-0.045*A**0.68)*(cos(sweep_LE))**0.15-3.1
K = 1/(pi*value("A")*Afactor*e)
C_f_e = value("C_f_e")#value("C_f_e")
C_D_0 = C_f_e*SwetSref#eval(designdata[19][ch]) 
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
##plt.show()
#print C_L_cr

string_liftdrag = ["C_L_cr","K","C_D_cr","LoverD","C_D_0"]
