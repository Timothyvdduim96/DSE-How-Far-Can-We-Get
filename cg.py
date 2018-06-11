from math import *
from wingvol import vol,b_cur,b_frac
#from WingLayout import c_r,c_t,lambdac_0,MAC
import numpy as np
#from Class_II_weight_estimation import *
#from Fuselage_Sizing import *
#from empennage import lh,b_h,sweep_h,ct_h,MAC_h,MAC_v
#from Enginesizing import ln

from parameters import *

l_cockpit = value("l_cockpit")
l_tail = value("l_tail")
l_cabin = value("l_cabin")
l_fus = value("l_fus")
MAC = value("MAC")
b = value("b")
c_r = value("c_r")
c_t = value("c_t")
d_ext_fus = 2.#value("d_ext_fus")
xstart = value("x_spar1")
xend = value("x_spar2")
lambdac_0 = value("lambdac_0")
sweep_h = value("sweep_h")
b_h = value("b_h")
ct_h = value("ct_h")
MAC_h = value("MAC_h")
MAC_v = value("MAC_v")
ln = value("ln")
x_oew = 24.
x_lemac = l_cabin*0.5 + l_cockpit - 0.25*MAC

#------------------------------------------OEW COMPONENTS-------------------------------------------

for i in range(2):
    
    def fus():
        x_cg = 0.435*l_fus
        w = value("W_fuselage")
        mom = x_cg*w

        return x_cg,w,mom

    def wing():
        span_pos = 0.35*b/2
        chord = c_r - (c_r-c_t)/((b-d_ext_fus/2)/2)*span_pos
        x_cg = chord*xstart+(xend-xstart)*0.7*chord + l_cabin*0.5 + l_cockpit - 0.25*MAC + cos(np.degrees(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2)))
        w = value("W_wing") #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def hortail():
        x_cg = l_fus - (cos(np.radians(sweep_h))*b_h/2 + ct_h) + cos(np.radians(sweep_h))*0.38*b_h/2 + 0.42*MAC_h
        w = value("W_empennage")/4 #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def verttail():
        x_cg = l_fus - 0.58*MAC_v
        w = value("W_empennage")/4*3 #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def engines():
        x_cg = x_lemac + cos(np.degrees(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))) - 0.3*ln
        w = value("W_propulsion") #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def nacelle():
        x_cg = x_lemac + cos(np.degrees(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))) - ln*0.4
        w = value("W_nacelle") #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def mainlandinggear():
        x_cg = x_oew + 0.804 #CHECK
        w = value("W_landinggear")/10.*9. #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def noselandinggear():
        w = value("W_landinggear")/10. #CHANGE
        x_cg = x_oew - (mainlandinggear()[0] - x_oew)*mainlandinggear()[1]/w
        mom = x_cg*w

        return x_cg,w,mom
        
    def fixedequipment ():
        w = value("W_equipment")
        x_cg = 846./866.*0.435*l_fus
        mom = x_cg*w
        
        return x_cg,w,mom

    x_oew_up = (fus()[2] + wing()[2] + hortail()[2] + verttail()[2] + engines()[2] + nacelle()[2] + mainlandinggear()[2] + noselandinggear()[2] + fixedequipment ()[2])/(fus()[1] + wing()[1] + hortail()[1] + verttail()[1] + engines()[1] + nacelle()[1] + mainlandinggear()[1] + noselandinggear()[1] + fixedequipment ()[1])
    print x_oew_up
    if i == 0:
        x_oew = x_oew_up

xcg_oew = x_oew_up
#----------------------------------------------FUEL-------------------------------------------------

vols = []

for i in range(len(vol)):
    vols.append(round(vol[i],3))

cgspan = float(vols.index(round(vol[len(vol)-1]/2,3)))/len(vols)*(float(len(vols))/len(b_cur))*b/2

dis1 = cos(np.degrees(lambdac_0))*cgspan

chord = c_r - (c_r-c_t)/((b-d_ext_fus/2)/2)*cgspan

xcg_fuel = dis1 + chord*(xstart+xend)/2 + x_lemac - cos(np.degrees(lambdac_0))*(c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))

#----------------------------------------------PAYLOAD----------------------------------------------

string_cg = ["x_lemac","xcg_oew","xcg_fuel"]
