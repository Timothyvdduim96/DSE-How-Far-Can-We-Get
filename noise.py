from parameters import *
from math import *
import matplotlib.pyplot as plt

rho_amb = 1.225
c       = 343.
V_land  = 93.8                 #approach speed
M_land  = V_land/c
mu      = 0.0000184
r       = 60.96                  #distance from source to observer [m]
thetha  = pi/2
phi     = 0.
Pe0     = (2.*10**-5)**2             #Reference pressure N/m2

flst    = []
pe_wlst = []
pe_slst = []
pe_flst = []
# Flst    = []
# Slst    = []
MGlst   = []
NGlst   = []
totlst  = []

#A-weighted lists
W_Alst  = []
S_Alst  = []
F_Alst  = []
MG_Alst  = []
NG_Alst  = []
tot_Alst  = []
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
bw  = value("b")
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

#ENGINES

approach_lst_SPL = [56.7,	66.1,	70.1,	72.8,	76.6,	73.0,	74.5,	77.0,	75.3,	72.2,	72.2,	71.2,	70.2,	70.0,	69.6,	71.1,	70.6,	67.1,	63.4,	63.5,	58.2,	51.5,	42.3,	37.7]
Takeoff_lst_SPL = [68.0,	63.1,	64.7,	71.2,	74.3,	75.0,	70.3,	72.6,	72.1,	73.3,	71.3,	70.7,	70.3,	70.0,	69.3,	68.0,	67.8,	66.3,	64.4,	62.0,	57.2,	52.2,	43.5,	33.1]
freq_lst = [50.,63.,80.,100.,125.,160.,200.,250.,315.,400.,500.,630.,800.,1000.,1250.,1600.,2000.,2500.,3150.,4000.,5000.,6300.,8000.,10000.]

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
    if S_f<2:
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
    SPL_total = 10*log10((10**(SPL_w/10)+10**(SPL_s/10)+10**(SPL_f/10)+10**(SPL_mg/10)+10**(SPL_ng/10)+10**(approach_lst_SPL/10)))
    totlst.append(SPL_total)

    #A-WEIGHTING CORRECTION
    delta_A = -145.528 + 98.262*log10(f) - 19.509*(log10(f))**2 + 0.975*(log10(f))**3
    
    L_A_i_w  = SPL_w + delta_A
    L_A_i_s  = SPL_s + delta_A
    L_A_i_f  = SPL_f + delta_A
    L_A_i_mg  = SPL_mg + delta_A
    L_A_i_ng  = SPL_ng + delta_A
    L_A_i_tot  = SPL_total + delta_A

    L_A_w = 10*log10(10**(L_A_i_w/10))
    L_A_s = 10*log10(10**(L_A_i_s/10))
    L_A_f = 10*log10(10**(L_A_i_f/10))
    L_A_mg = 10*log10(10**(L_A_i_mg/10))
    L_A_ng = 10*log10(10**(L_A_i_ng/10))
    L_A_tot = 10*log10(10**(L_A_i_tot/10))

    W_Alst.append(L_A_w)
    S_Alst.append(L_A_s)
    F_Alst.append(L_A_f)
    MG_Alst.append(L_A_mg)
    NG_Alst.append(L_A_ng)
    tot_Alst.append(L_A_tot)

#NORMAL PLOTS

# plt.plot(flst,pe_wlst,label = 'Clean wing')
# plt.plot(flst,pe_slst,label = 'Slats')
# plt.plot(flst,pe_flst,label = 'Flaps')
# plt.plot(flst,MGlst,label = 'Main landing gear')
# plt.plot(flst,NGlst,label = 'Nose landing gear')
plt.plot(flst,totlst,label = 'Total')
plt.plot(freq_lst,approach_lst_SPL, label = 'Engines')

plt.xscale('log')
plt.legend(loc=4)
plt.ylabel("SPL [dB]")
plt.xlabel("Frequency [Hz]")
plt.axis((10**1,10**4,0,100))
plt.show()


#A_WEIGHTED PLOTS

# plt.plot(flst,W_Alst,label = 'Clean wing ')
# plt.plot(flst,S_Alst,label = 'Slats')
# plt.plot(flst,F_Alst,label = 'Flaps wing')
# plt.plot(flst,MG_Alst,label = 'Main landing gear')
# plt.plot(flst,NG_Alst,label = 'Nose landing gear')
# plt.plot(flst,tot_Alst,label = 'Total')

# plt.xscale('log')
# plt.legend(loc=4)
# plt.ylabel("SPL [dBA]")
# plt.xlabel("Frequency [Hz]")
# plt.axis((10**0,10**4,0,100))
# plt.show()

