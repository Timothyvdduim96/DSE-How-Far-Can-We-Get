from math import pi

T = 213000./2
T_ref = 146330.
dfan_ref = 2152.
dcore_ref = 1084.
dnacelle_ref = 2520.
bypass_ref = 11.
bypass_own = 14.
mdot_ref = 466. #CFM56
dfan_refCFM = 1836.
rho = 1.225
V0 = 0
length_ref_t = 5.44
lnosecowl_ref = 0.67
lfancowl_ref = 1.58 
laft_ref = 1.98
lprimnozzle_ref = 0.23
lplug_ref = 0.98


dcore_own = (T/T_ref)*dcore_ref
ratio_ref = dfan_ref/dcore_ref
ratio_own = (bypass_own*ratio_ref)/bypass_ref
dfan_own = ratio_own*dcore_own
dnacelle_own = (dnacelle_ref/dfan_ref)*dfan_own
Afan_own = pi*(dfan_own/2/1000)**2

ltotal = length_ref_t*(T/T_ref)
lnosecowl = lnosecowl_ref *(T/T_ref)
lfancowl = lfancowl_ref *(T/T_ref)
laft = laft_ref*(T/T_ref)
lprimnozzle = lprimnozzle_ref * (T/T_ref)
lplug = lplug_ref* (T/T_ref)

mdot_own = (mdot_ref*dfan_own)/dfan_refCFM
V = mdot_own/(rho*Afan_own)
Vj = T/(rho*Afan_own*V)+V0



print T/T_ref
print dcore_own
print dfan_own
print dnacelle_own
print ltotal

