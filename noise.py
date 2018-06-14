from parameters import value
from math import cos, sin, pi
import matplotlib.pyplot as plt

rho_amb = 1.225
c = 343.
V_land = 93.8 #approach speed
M_land = V_land/c
mu = 0.0000184
r = 50.                  #distance from source to observer
thetha = pi
phi = pi

flst = []
pe_wlst = []
pe_slst = []
pe_flst = []
Flst = []
Slst = []

#----------------------------------
def pe2(F):
    pe=(rho_amb*c*P_w*D_w*F)/(4*pi*r**2*(1-M_land*cos(thetha))**4)
    return pe

def P(K,a,G):
    P = K*M_land**a*G*rho_amb*c**3*bw**2
    return P

#---------------------------------

#CLEAN WING - LANDING

V = 93.8        #approach speed
M = V/c

#CLEAN WING AND SLATS
bw = value("b")
A_w = value("S")
G_w = 0.37*(A_w/bw**2)*((rho_amb*M_land*c*A_w)/(mu*bw))**-0.2
L_w = G_w*bw
K_w = 4.464*10**-5
a_w = 5.
P_w = P(K_w,a_w,G_w)
D_w = 4*cos(phi)**2*cos(thetha/2)**2

#FLAPS
delta_f = pi/5
A_f     = 20 #!!!!
b_f     = 4  #!!!!
G_f     = (A_f/bw**2)*sin(delta_f)**2
L_f     = A_f/b_f
K_f     = 2.787*10**-4
a_f     = 6.
P_f     = P(K_f,a_f,G_f)
D_f     = 3*(sin(delta_f)*cos(thetha)+cos(delta_f)*sin(thetha)*cos(phi))**2

#MAIN LANDING GEAR

d    = 1.27 
n    = 4.
G_mg = n*(d/bw)**2
L_mg = d
# K_mg = 

for f in range(0,10**4,5):
    S_w = (f*L_w*(1-M_land*cos(thetha)))/(M_land*c)
    Fw = 0.613*(10*S_w)**4*((10*S_w)**1.5+0.5)**-4
    pe_w= pe2(Fw)
    flst.append(f)
    pe_wlst.append(pe_w)
    #SLATS
    Fs = 0.613*(10*S_w)**4*((10*S_w)**1.5+0.5)**-4 + 0.613*(2.19*S_w)**4*((2.19*S_w)**1.5+0.5)**-4
    pe_s = pe2(Fs)
    pe_slst.append(pe_s)
    #FLAPS
    S_f = (f*L_f*(1-M_land*cos(thetha)))/(M_land*c)
    if S_f<20:
        Ff = 0.0480*S_f
    elif 2<=S_f<=20:
        Ff = 0.1406*S_f**-0.55
    elif S_f>20:
        Ff = 216.49*S_f**-3
    pe_f = pe2(Ff)
    pe_flst.append(pe_f)




# plt.plot(Slst,Flst)
plt.plot(flst,pe_wlst)
plt.plot(flst,pe_slst)
plt.plot(flst,pe_flst)
plt.xscale('log')
# plt.yscale('log')
plt.show()