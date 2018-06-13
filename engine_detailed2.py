from math import pi

T = 213000./2
T_ref = 146330.
dfan_ref = 2152.
dcore_ref = 1084.
bypass_ref = 11.
bypass_own = 14.
mdot_ref = 466. #CFM56
dfan_refCFM = 1836.
rho = 1.225
V0 = 0


dcore_own = (T/T_ref)*dcore_ref
ratio_ref = dfan_ref/dcore_ref
ratio_own = (bypass_own*ratio_ref)/bypass_ref
dfan_own = ratio_own*dcore_own
Afan_own = pi*(dfan_own/2/1000)**2

mdot_own = (mdot_ref*dfan_own)/dfan_refCFM
V = mdot_own/(rho*Afan_own)
Vj = T/(rho*Afan_own*V)+V0

print dfan_own