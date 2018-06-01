#---------Engine Sizing Program---------------

import numpy as np
from math import *

#Parameters

T      = 170000.                 #take-off thrust [N]
T_ref  = 120400.                 #take-off thrust reference [N]
D_ref  = 2.543                   #engine diameter reference [m]
W_ref  = 3153.                   #engine weight reference [kg]
l_ref  = 3.328                   #engine length [m]
a_eng  = 1.                      #is 1 as preliminary assumption, can vary between 0.8 and 1.3
N_eng  = 2.                      #number of engines
lamda  = 18.                     #bypass ratio
n_nozz = 0.97                    #nozzle efficiency
n_tf   = 0.75                    #efficiency of turbine and fan
gamma  = 1.4                 
R      = 287     
T_0    = 288.15                  #standard ISA temperature at sea level
a0     = sqrt(gamma*R*T_0)       #speed of sound at sea level ISA
rho_0  = 1.225                   #density at sea level ISA
Temp_4 = 1350.                   #turbine inlet temperature, between 1350 - 1650K, depends on technologie used
G_eng  = (Temp_4/600.)-1.25      #specific gas generator power 
Cl_eng = 7.8                     #standard parameter for categorie C engine
delta_l= 0.10                    #standard parameter for categorie C engine
phi_eng= 0.75                    #should be selected based on experience/assumption, 0.5 - 0.75
Beta   = 0.21+(0.12/sqrt(phi_eng-0.3)) #standard parameter for categorie C engine
eta    = 0.32

#-------------------------------------------------------------------------------
#Engine basic sizes


SF = T/T_ref
D = sqrt(SF)*D_ref 
W_eng = (SF**a_eng)*W_ref 
l = (SF**(a_eng-0.5))*l_ref
mdot = (T/(N_eng*a0))*((1+lamda)/sqrt(5*n_nozz*G_eng*(1+n_tf*lamda)))  #massflow
Ds_over_Di = 0.05*(1+(0.1*rho_0*a0/mdot)+((3*lamda)/(1+lamda))) #inlet to spinner ratio
Di = 1.65*sqrt(((mdot/(rho_0*a0))+0.005)/(1-Ds_over_Di**2))     #inlet diameter
Dh = Di                                                        #highlight diameter
ln = Cl_eng*(sqrt((mdot/(rho_0*a0))*((1+0.2*lamda)/(1+lamda)))+delta_l) #nacelle length
lf = phi_eng*ln                                                    #fan cowl length
Dn = Di+0.06*phi_eng*ln+0.03                                       #maximum nacelle diameter
Def = Dn*(1-(1/3)*phi_eng**2)                                      #exit diameter fan
lg = (1-phi_eng)*ln                                                #exposed length of gas generator
Dg = Def*((((0.089*mdot*lamda)/(rho_0*a0))+4.5)/(((0.067*mdot*lamda)/(rho_0*a0))+5.8))**2  #gas generator cowling diameter at fan exit
Deg = 0.55*Dg                                                  #gas generator cowling diameter at gas generator exit
Betalf = Beta * lf                                             #position of max diameter

print
print "engine weight = ",W_eng,"kg"
print
print "massflow = ", mdot, "kg/s"
print
print "inlet diameter = ",Di, "m"
print
print "highlight diameter (Dh) = ",Dh, "m"
print
print "maximum nacelle diameter (Dn) = ", Dn, "m"
print
print "exit diameter fan (Def) = ",Def, "m"
print
print "gas generator diameter at fan exit (Dg) = ", Dg, "m"
print
print "gas generator diameter at gas generator exit (Deg) = ", Deg, "m"
print
print "nacelle length (ln) = ",ln, "m"
print
print "fan cowl length (lf) = ",lf, "m"
print
print "position of max diameter = ",Betalf, "m"

#-------------------------------------------------------------------------------
#Position of engine on wing

yawmoment_1engine = T/2*eta



