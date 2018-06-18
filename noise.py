from parameters import value
from math import *
import matplotlib.pyplot as plt

rho_amb = 1.225
c       = 343.
V_land  = 93.8                 #approach speed
M_land  = V_land/c
mu      = 0.0000184
r       = 50.                  #distance from source to observer
thetha  = pi/2
phi     = 0.
Pe0     = (2.*10**-5)**2             #Reference pressure N/m2

flst    = []
pe_wlst = []
pe_slst = []
pe_flst = []
Flst    = []
Slst    = []
MGlst   = []
NGlst   = []
totlst  = []

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
delta_f = value("d_f_land")/(180/pi)
A_f     = value("S_flaps_land")
b_f     = 2*(value("bf_o")-value("bf_i"))
G_f     = (A_f/bw**2)*sin(delta_f)**2
L_f     = A_f/b_f
K_f     = 2.787*10**-4
a_f     = 6.
P_f     = P(K_f,a_f,G_f)
D_f     = 3*(sin(delta_f)*cos(thetha)+cos(delta_f)*sin(thetha)*cos(phi))**2

#LANDING GEAR

d    = 1.27 
n    = 2.
G_mg = n*(d/bw)**2
L_mg = d
K_mg = 4.349*10**-4
a_mg = 6.
P_mg = P(K_mg,a_mg,G_mg)
D_mg = (3/2)*sin(thetha)**2

for f in range(1,10**4,1):
    S_w = (f*L_w*(1-M_land*cos(thetha)))/(M_land*c)
    Fw = 0.613*(10*S_w)**4*((10*S_w)**1.5+0.5)**-4
    pe_w = pe2(Fw)
    SPL_w = 10*log10(pe_w/Pe0)
    flst.append(f)
    pe_wlst.append(SPL_w)
    #SLATS
    Fs = 0.613*(10*S_w)**4*((10*S_w)**1.5+0.5)**-4 + 0.613*(2.19*S_w)**4*((2.19*S_w)**1.5+0.5)**-4
    pe_s = pe2(Fs)
    SPL_s = 10*log10(pe_s/Pe0)
    pe_slst.append(SPL_s)
    #FLAPS
    S_f = (f*L_f*(1-M_land*cos(thetha)))/(M_land*c)
    if S_f<20:
        Ff = 0.0480*S_f
    elif 2<=S_f<=20:
        Ff = 0.1406*S_f**-0.55
    elif S_f>20:
        Ff = 216.49*S_f**-3
    pe_f = pe2(Ff)
    SPL_f = 10*log10(pe_f/Pe0)
    pe_flst.append(SPL_f)
    #MAIN LANDING GEAR
    S_mg = (f*L_mg*(1-M_land*cos(thetha)))/(M_land*c)
    Fmg = 2*(13.59*S_mg**2*(S_mg**2+12.5)**-2.25)
    pe_mg = pe2(Fmg)
    SPL_mg = 10*log10(pe_mg/Pe0)
    MGlst.append(SPL_mg)
    #NOSE LANDING GEAR
    Fng = 13.59*S_mg**2*(S_mg**2+12.5)**-2.25
    pe_ng = pe2(Fng)
    SPL_ng = 10*log10(pe_ng/Pe0)
    NGlst.append(SPL_ng)
    #TOTAL
    SPL_total = 10*log10((10**(SPL_w/10)+10**(SPL_s/10)+10**(SPL_f/10)+10**(SPL_mg/10)+10**(SPL_ng/10)))
    totlst.append(SPL_total)


plt.plot(flst,pe_wlst,label = 'Clean wing')
plt.plot(flst,pe_slst,label = 'Slats')
plt.plot(flst,pe_flst,label = 'Flaps')
plt.plot(flst,MGlst,label = 'Main landing gear')
plt.plot(flst,NGlst,label = 'Nose landing gear')
plt.plot(flst,totlst,label = 'Total')
plt.xscale('log')
plt.legend(loc=4)
# plt.grid('True')
plt.show()

