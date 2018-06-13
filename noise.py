from parameters import value

rho_amb = 1.225
c = 343.
V_land = 93.8 #approach speed
M_land = V_land/c
mu = 0.0000184
r = 50                  #distance from source to observer
bw = value("b")
Aw = value("S")



#CLEAN WING - LANDING

V = 93.8        #approach speed
M = V/c
G_w = 0.37*(Aw/bw**2)*((rho_amb*M_land*c*Aw)/(mu*bw))**-0.2
L_w = G_w*bw
K_w = 4.464*10**-5
a_w = 5
P_w = K_w*M_land**a_w*G_w*rho_amb*c**3*bw**2

for f in range(0,10**4,5):
    S=(f*L_w*(1-M_land*))