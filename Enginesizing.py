import numpy as np
from math import *

#Engine Sizing Program

T      = 170000.                  #take-off thrust [N]
T_ref  = 156000.                  #take-off thrust reference [N]
D_ref  = 2.543                   #engine diameter reference [m]
W_ref  = 3153.                    #engine weight reference [kg]
l_ref  = 3.328                   #engine length [m]
a      = 1.                       #is 1 as preliminary assumption, can vary between 0.8 and 1.3
N      = 2.                       #number of engines
lamda  = 18.                      #bypass ratio
n_nozz = 0.97                    #nozzle efficiency
n_tf   = 0.75                    #efficiency of turbine and fan
gamma  = 1.4                 
R      = 287.     
Temp_0 = 288.15                  #standard ISA temperature at sea level
a0     = sqrt(gamma*R*Temp_0)    #speed of sound at sea level ISA
rho0   = 1.225                   #density at sea level ISA
Temp_4 = 1350.                    #turbine inlet temperature, between 1350 - 1650K, depends on technologie used
G      = (Temp_4/600)-1.25       #specific gas generator power 
Cl     = 9.8                     #standard parameter for categorie B engine
delta_l= 0.05                    #standard parameter for categorie B engine
Beta   = 0.35                    #standard parameter for categorie B engine
phi    = 0.75                    #should be selected based on experience/assumption, 0.5 - 0.75

#-------------------------------------------------------------------------------

SF = T/T_ref
D = sqrt(SF)*D_ref
W = (SF**a)*W_ref 
l = (SF**(a-0.5))*l_ref
mdot = (T/(N*a0))*((1+lamda)/sqrt(5*n_nozz*G*(1+n_tf*lamda)))  #massflow
Ds_over_Di = 0.05*(1+(0.1*rho0*a0/mdot)+((3*lamda)/(1+lamda))) #inlet to spinner ratio
Di = 1.65*sqrt(((mdot/(rho0*a0))+0.005)/(1-Ds_over_Di**2))     #inlet diameter
Dh = Di                                                        #highlight diameter
ln = Cl*(sqrt((mdot/(rho0*a0))*((1+0.2*lamda)/(1+lamda)))+delta_l) #nacelle length
lf = 
