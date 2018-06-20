from math import sqrt
print
print
#--------CONSTANTS---------
B         = 14.        #Bypass ratio
PR_tot    = 30.        #Total compressor pressure ratio
PR_fan    = 1.4        #Pressure ratio fan
TET       = 1600.      #Turbine entry temperature [K]

T0        = 216.       #Ambient temperature [K]
gamma     = 1.4
M0        = 0.       #Flight mach number
Pr_intake = 0.95       #Pressure recovery factor intake
eta_pol   = 0.85       #Polytropic efficiency
R         = 287.
g         = 9.81
eta_mech  = 0.98
cp        = 1005.
eta_b     = 0.96       #Combustion efficiency
H         = 4.31*10**7 #Fuel calorific value
#----------------------------

Tt2 = T0*(1+(gamma-1)*M0**2/2)

Pt2_over_P0 = Pr_intake*(1+(gamma-1)*M0**2/2)**(gamma/(gamma -1)) #Pressure ratio at station 2

Tt3 = Tt2*PR_fan**((gamma-1)/(eta_pol*gamma))                    #Fan exit temperature

Pt3_over_P0 = PR_fan * Pt2_over_P0                               #Cold nozzle pressure ratio

Pt3_over_P8 = ((gamma+1)/2)**(gamma/(gamma -1))                  #Critical pressure ratio     

P8_over_P0 = Pt3_over_P0/Pt3_over_P8

print Pt3_over_P0, Pt3_over_P8
if Pt3_over_P0 > Pt3_over_P8:
    print "cold nozzle is choked"
    #print "assume M8 = 1"
    print
    M8 = 1.

    T8 = Tt3*(2/(gamma+1))

    w8 = M8*sqrt(gamma*R*T8)        #Cold nozzle outlet velocity

    v0 = M0*sqrt(gamma*R*T0)

    Tc_over_mg = (B/(B+1))*(1/g)*((w8-v0)+sqrt((R*T8)/gamma)*(1-(1/P8_over_P0))) #specific thrust of cold flow

    

elif Pt3_over_P0 < Pt3_over_P8:
    print "cold nozzle is not choked"

    M8 = sqrt((2/gamma-1)*(Pt3_over_P0**((gamma-1)/gamma)-1))

    T8 = Tt3/(Pt3_over_P0**((gamma-1)/gamma))

    w8 = M8*sqrt(gamma*R*T8)        #Cold nozzle outlet velocity

    v0 = M0*sqrt(gamma*R*T0)

    Tc_over_mg = (B/(B+1))*(1/g)*((w8-v0)) #specific thrust of cold flow



Pt4_over_Pt3 = PR_tot/PR_fan    #Pressure ratio high pressure compressor

Tt4 = Tt3*(Pt4_over_Pt3)**((gamma-1)/(eta_pol*gamma))        #Total temperature at outlet of HPC

Tt6 = TET - (1/eta_mech)*(Tt4-Tt3)      #Temperature behind HPT

Tt7 = Tt6 - ((B+1)/eta_mech)*(Tt3-Tt2)  #Temperature behind LPT

Pt7_over_Pt5 = (Tt7/TET)**(gamma/(eta_pol*(gamma-1)))

Pt5_over_Pt4 = 0.95    #Pressure loss in combustion chamber (ASSUMPTION)

Pt7_over_P0 = Pt7_over_Pt5*Pt5_over_Pt4*Pt4_over_Pt3*Pt3_over_P0 #Hot nozzle pressure ratio

Pe_over_P0 = Pt7_over_P0/Pt3_over_P8

print Pt7_over_P0
if Pt7_over_P0 > Pt3_over_P8:
    print "hot nozzle is choked"
    #print "assume Me = 1"
    print
    Me = 1.

    Te = Tt7*(2/(gamma+1))  #Temperature at exit

    we = Me*sqrt(gamma*R*Te)        #Jet velocity of hot stream

    Th_over_mg = (1/(B+1))*(1/g)*((we-v0)+sqrt((R*Te)/gamma)*(1-(1/Pe_over_P0)))  #Specific thrust of hot flow


if Pt7_over_P0 < Pt3_over_P8:
    print "hot nozzle is not choked"
    print
    Me = sqrt((2/gamma-1)*(Pt7_over_P0**((gamma-1)/gamma)-1))

    Te = Tt7/(Pt7_over_P0**((gamma-1)/gamma)) #Temperature at exit

    we = Me*sqrt(gamma*R*Te)        #Jet velocity of hot stream

    Th_over_mg = (1/(B+1))*(1/g)*((we-v0))  #Specific thrust of hot flow


ST_tot = Tc_over_mg + Th_over_mg    #total specific thrust

SFC = (1/(1+B))*(cp/(H*eta_b)*3600)*((TET-Tt4)/ST_tot) #Specific fuel consumption

Thrust = ST_tot*(550.*g)


print Thrust
print we, v0
# print w8
# print we
# print Pe_over_P0*19677.3, Te
# print T8