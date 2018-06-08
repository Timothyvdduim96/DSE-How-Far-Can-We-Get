from math import *
import numpy as np

parameter = open("parameters.txt","w")

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
C_f_e = 0.003                       #friction coefficient
V_s = 100.                          #stall speed based on reference aircraft
V_rot = 1.1                         #rotation speed
n_max = 2.5                         #max load factor (CS25)
f = 0.9745                          #fuel fraction during cruise

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
#parameter.write("f "+str(f)+"\n")

#from testpar import *
from TWWS import *

#for i in range(len(string_testpar)):
#    parameters.write(string_testpar[i] + " " + str(eval(string_testpar[i])) + "\n")

for i in range(len(string_TWWS)):
    print i
    parameter.write(string_TWWS[i] + " " + str(eval(string_TWWS[i])) + "\n")

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
