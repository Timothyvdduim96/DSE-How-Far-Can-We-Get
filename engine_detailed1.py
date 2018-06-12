from math import sqrt

#-------CONSTANTS--------------

Cr_alt    = 15.                   #Cruise altitude [km] #11.8872
M0        = 1.39                  #Cruise speed [M]
M_dot_air = 96.                   #Air mass flow rate [kg/s]
eta_inlet = 0.97                  #Intake insentropic efficiency
pr_fan    = 2.15                  #Fan pressure ratio
eta_fan   = 0.87                  #Fan isentropic efficiency
labda     = 5.                    #Bypass ratio
eta_LPC   = 0.9                   #LPC isentropic efficiency
eta_HPC   = 0.87                  #HPC isentropic efficiency
eta_LPT   = 0.9                   #LPT isentropic efficiency
eta_HPT   = 0.89                  #HPT isentropic efficiency
eta_mech  = 0.99                  #Mechanical efficieny of high and low speed shaft
eta_gear  = 0.995                 #Mechanical efficieny of gearbox
eta_cc    = 0.99                  #Combuster efficiency
pr_LPC    = 3.5                   #LPC pressure ratio
pr_HPC    = 9.5                   #HPC pressure ratio
eta_nozz  = 0.98                  #nozzle efficiency
pr_comb   = 0.96                  #Combuster pressure ratio
T04       = 1833.                 #Combuster exit temperature 
T_amb     = 216.                  #Ambient temperature [K]
P_amb     = 12111.                #Ambient pressure [Pa]
R         = 287.                  #Gas constant [J/Kg*K]
LHV       = 43. * 10**6           #Fuel calorific value [J/kg]
cp_air    = 1000.                 #Specific heat air [J/kg*K]
cp_gas    = 1150.                 #Specific heat gas [J/kg*K]
k_air     = 1.4                   #Ratio of specific heat for air
k_gas     = 1.33                  #Ratio of specific heat for gas

v0 = M0*sqrt(k_air*R*T_amb)

#-----EQUATIONS---------------

T00 = T_amb*(1+(((k_air-1)/2)*M0**2))

P00 = P_amb*(T00/T_amb)**(k_air/(k_air-1))

T021 = T00*(1+(1/eta_fan)*(pr_fan**((k_air-1)/k_air)-1))

P0_inlet = (P_amb*(1+(eta_inlet*((k_air-1)/2)*M0**2))**(k_air/(k_air-1)))

P021 = pr_fan * P0_inlet

M_dot_hot = M_dot_air/(labda+1)

M_dot_cold = M_dot_air - M_dot_hot

T025 = T021*(1+(1/eta_LPC)*(pr_LPC**((k_air-1)/k_air)-1))

P025 = pr_LPC*P021

T03 = T025*(1+(1/eta_HPC)*(pr_HPC**((k_air-1)/k_air)-1))

P03 = pr_HPC*P025

P04 = pr_comb * P03

W_fan = M_dot_air*cp_air*(T021 - T00)
W_LPC = M_dot_hot*cp_air*(T025 - T021)
W_HPC = M_dot_hot*cp_air*(T03 - T025)

W_HPT = W_HPC/eta_mech

M_dot_fuel = (M_dot_hot*cp_gas*(T04 - T03))/(eta_cc*LHV)

M_dot_comb = M_dot_hot + M_dot_fuel

T045 = T04 - W_HPT/(M_dot_comb*cp_gas)

pr_HPT = (-((((T045/T04)-1)/-eta_HPT)-1))**(k_gas/(k_gas-1))

P045 = pr_HPT*P04

W_LPT = (W_LPC/(eta_mech))+(W_fan/(eta_mech*eta_gear))

T05 = T045 - (W_LPT/(M_dot_comb*cp_gas))

pr_LPT = (-((((T05/T045)-1)/-eta_LPT)-1))**(k_gas/(k_gas-1))

P05 = pr_LPT * P045

pr_crit_nozz = 1/((1-(1/eta_nozz)*((k_gas-1)/(k_gas+1)))**(k_gas/(k_gas-1)))

if (P05/P_amb) > pr_crit_nozz:
    print "nozzle of the core is choked"

pr_crit_fan = 1/(1-(k_air-1)/(eta_nozz*(k_air+1)))**(k_air/(k_air-1)) 

if (P021/P_amb) > pr_crit_fan:
    print "nozzle of the fan is choked"

T8 = T05*(2/(k_gas+1))

P8 = P05/(pr_crit_nozz)

T18 = T021 * (2/(k_air+1))

P18 = P021/pr_crit_fan

v8 = sqrt(k_gas*R*T8)

v18 = sqrt(k_air*R*T18)

A8 = (M_dot_comb*R*T8)/(P8*v8)

A18 = (M_dot_cold*R*T18)/(P18*v18)

T_fan = M_dot_cold*(v18-v0) + A18*(P18-P_amb)

T_core = M_dot_comb*(v8-v0) + A8*(P8-P_amb)

T_total = T_fan + T_core

SFC = M_dot_fuel/T_total


print
print
print "Nozzle area = ",A8, "m2"
print
print "Exit fan area = ",A18, "m2"
print
print "Total thrust = ",T_total, "N"
print
print "Specific Fuel Consumption = ", SFC, "kg/N*s"