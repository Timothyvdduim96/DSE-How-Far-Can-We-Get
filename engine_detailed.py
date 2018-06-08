#-------CONSTANTS--------------

Cr_alt    = 40000                 #Cruise altitude [m]
Cr_spd    = 0.79                  #Cruise speed [M]
M_dot_air = 96                    #Air mass flow rate [kg/s]
eta_inlet = 0.97                  #Intake insentropic efficiency
pr_fan    = 2.15                  #Fan pressure ratio
eta_fan   = 0.87                  #Fan isentropic efficiency
labda     = 14                    #Bypass ratio
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
T_comb_ext= 1883                  #Combuster exit temperature T0,4
T_amb     = 216                   #Ambient temperature [K]
P_amb     = 12111                 #Ambient pressure [Pa]
R         = 287                   #Gas constant [J/Kg*K]
LHV       = 43                    #Fuel calorific value [MJ/kg]
cp_air    = 1000                  #Specific heat air [J/kg*K]
cp_gas    = 1150                  #Specific heat gas [J/kg*K]
k_air     = 1.4                   #Ratio of specific heat for air
k_gas     = 1.33                  #Ratio of specific heat for gas


#-----EQUATIONS---------------

TOO = T_amb*(1+(((k_air-1)/2)*Cr_alt**2))
print TOO