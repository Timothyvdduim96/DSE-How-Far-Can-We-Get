from math import *
import numpy as np

#from TWWS import * #CHECK
from class_II_final_version import * #CHECK
from Class_I import * #CHECK
from Enginesizing import * #CHECK
from Fuselage_Sizing import * #CHECK
from wingvol import * #CHECK
from wing_layout import * #CHECK
from emissions import * #CHECK
from liftdrag import * #CHECK
from empennage import * #CHECK
from landing_gear import * #CHECK
from airfoil2 import * #CHECK
from cg import *
from Drag import *
#------------------------------------------------CONVERSION--------------------------------------------------

lbf_to_N = 4.4482216
hr_to_s = 3600.
lbm_to_kg = 0.45359237
ft_to_km = 0.3048/1000
ft_to_m = 0.3048
gal_to_L = 3.78541
FL_to_m = ft_to_m*100
rad_to_deg = 180/pi
inch_to_cm=2.54
cm_to_inch=1/2.54
mm_to_m=1./1000.
m_to_mm=1000.
cm_to_m=1/100.
inch_to_m=inch_to_cm*cm_to_m


M_tf = 0.935                        #technology factor for supercritical airfoils
FL = 390                            #flight level
h_cr = FL*FL_to_m                   #cruise altitude
R = 287.05
g = 9.80665                         #gravitational acc.
gamma = 1.4
M_cr = 0.79                         #cruise mach number (req)
M_max = 0.82                        #maximum cruise mach number
rho_0 = 1.225                       #sea-level density
T_0 = 288.15                        #sea-level temperature 
s_l = 2000.                         #landing distance
V_land = sqrt(s_l/0.5847)           #landing velocity based on landing distance
cV = 0.024                          #climb gradient requirement from CS25
A = 14.                             #Aspect ratio
c = 17.                             #climb rate as from ref. aircraft
C_f_e = 0.0026                      #friction coefficient
V_s = 100.                          #stall speed based on reference aircraft
V_rot = 1.1                         #rotation speed
n_max = 2.5                         #max load factor (CS25)
f = 0.9745                          #fuel fraction during cruise
SwetSref = 5.5

parameter = open("parameters.txt","w")
parameter.write("M_tf "+str(M_tf)+"\n")
parameter.write("FL "+str(FL)+"\n")
parameter.write("h_cr "+str(h_cr)+"\n")
parameter.write("R "+str(R)+"\n")
parameter.write("g "+str(g)+"\n")
parameter.write("gamma "+str(gamma)+"\n")
parameter.write("M_cr "+str(M_cr)+"\n")
parameter.write("M_max "+str(M_max)+"\n")
parameter.write("rho_0 "+str(rho_0)+"\n")
parameter.write("T_0 "+str(T_0)+"\n")
parameter.write("s_l "+str(s_l)+"\n")
parameter.write("V_land "+str(V_land)+"\n")
parameter.write("cV "+str(cV)+"\n")
parameter.write("A "+str(A)+"\n")
parameter.write("c "+str(c)+"\n")
parameter.write("C_f_e "+str(C_f_e)+"\n")
parameter.write("V_s "+str(V_s)+"\n")
parameter.write("V_rot "+str(V_rot)+"\n")
parameter.write("n_max "+str(n_max)+"\n")
parameter.write("f "+str(f)+"\n")
#parameter.write("P_c "+str(P_c)+"\n")
parameter.write("x_spar1 "+str(0.25)+"\n")
parameter.write("x_spar2 "+str(0.55)+"\n")
parameter.write("Afactor "+str(1.2)+"\n")
parameter.write("e "+str(0.85)+"\n")
parameter.write("MTOW "+str(67834.)+"\n")
parameter.write("S "+str(110.)+"\n")
parameter.write("thrust "+str(213.)+"\n")
parameter.write("SwetSref "+str(SwetSref)+"\n")

#for i in range(len(string_TWWS)):
#    parameter.write(string_TWWS[i] + " " + str(eval(string_TWWS[i])) + "\n")

for i in range(len(string_class_II_final_version)):
    parameter.write(string_class_II_final_version[i] + " " + str(eval(string_class_II_final_version[i])) + "\n")

for i in range(len(string_class_I)):
    parameter.write(string_class_I[i] + " " + str(eval(string_class_I[i])) + "\n")

for i in range(len(string_enginesizing)):
    parameter.write(string_enginesizing[i] + " " + str(eval(string_enginesizing[i])) + "\n")

for i in range(len(string_Fuselage_Sizing)):
    parameter.write(string_Fuselage_Sizing[i] + " " + str(eval(string_Fuselage_Sizing[i])) + "\n")

for i in range(len(string_wing_layout)):
    print eval(string_wing_layout[i])
    parameter.write(string_wing_layout[i] + " " + str(eval(string_wing_layout[i])) + "\n")

for i in range(len(string_wingvol)):
    parameter.write(string_wingvol[i] + " " + str(eval(string_wingvol[i])) + "\n")

for i in range(len(string_emissions)):
    parameter.write(string_emissions[i] + " " + str(eval(string_emissions[i])) + "\n")

for i in range(len(string_liftdrag)):
    parameter.write(string_liftdrag[i] + " " + str(eval(string_liftdrag[i])) + "\n")

for i in range(len(string_empennage)):
    parameter.write(string_empennage[i] + " " + str(eval(string_empennage[i])) + "\n")

for i in range(len(string_landing_gear)):
    parameter.write(string_landing_gear[i] + " " + str(eval(string_landing_gear[i])) + "\n")

for i in range(len(string_airfoil2)):
    parameter.write(string_airfoil2[i] + " " + str(eval(string_airfoil2[i])) + "\n")

for i in range(len(string_cg)):
    parameter.write(string_cg[i] + " " + str(eval(string_cg[i])) + "\n")

for i in range(len(string_drag)):
    parameter.write(string_drag[i] + " " + str(eval(string_drag[i])) + "\n")


parameter.close()

#from testpar import *

file = 'parameters.txt'
file = np.genfromtxt(file, dtype=str, delimiter=';')
lst = []
checkdoubles = []
count = []
doubles = []
found = False

for i in range(len(file)):
    lst.append(file[i].split())

for i in range(len(lst)):
    checkdoubles.append(lst[i][0])
    count.append(checkdoubles.count(lst[i][0]))
    if checkdoubles.count(lst[i][0]) > 1:
        doubles.append([lst[i][0],checkdoubles.count(lst[i][0])])
