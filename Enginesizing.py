import numpy as np
from math import *

#Engine Sizing Program

T      = 170000                  #take-off thrust [N]
T_ref  = 12000                   #take-off thrust reference [N]
D_ref  = 3                       #engine diameter reference [m]
W_ref  = 40000                   #engine weight reference [kg]
l_ref  = 3                       #engine length [m]
a      = 1                       #is 1 as preliminary assumption, can vary between 0.8 and 1.3
N      = 2                       #number of engines
lamda  = 18                      #bypass ratio
n_nozz = 0.97                    #nozzle efficiency
n_tf   = 0.75                    #efficiency of turbine and fan
gamma  = 1.4                 
R      = 287     
Temp_0 = 288.15                  #standard ISA temperature at sea level
a0     = sqrt(gamma*R*Temp_0)    #speed of sound at sea level
Temp_4 = 1350                    #turbine inlet temperature, between 1350 - 1650K, depends on technologie used
G      = (Temp_4/600)-1.25       #specific gas generator power 
#-------------------------------------------------------------------------------

SF = T/T_ref
D = sqrt(SF)*D_ref
W = (SF**a)*W_ref 
l = (SF**(a-0.5))*l_ref
mdot = (T/(N*a0))*((1+lamda)/sqrt(5*n_nozz*G*(1+n_tf*lamda)))
Ds_over_Di = 