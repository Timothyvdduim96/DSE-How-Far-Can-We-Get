from math import *
from wingvol import a,xstart,xend,c_r_f,c_t_f,b,vol,b_cur,d_ext_fus
from WingLayout import c_r,c_t,lambdac_0,MAC
import numpy as np
from Class_II_weight_estimation import *
from Fuselage_Sizing import l_nosecone,l_tailcone,l_cabin
from empennage import lh,b_h,sweep_h,ct_h,MAC_h,MAC_v
from Enginesizing import ln

l_fus = l_nosecone + l_tailcone + l_cabin
x_oew = 25.

#------------------------------------------OEW COMPONENTS-------------------------------------------

for i in range(2):
    
    def fus():
        x_cg = 0.435*l_fus
        w = W_fus/kglbs
        mom = x_cg*w

        return x_cg,w,mom

    def wing():
        span_pos = 0.35*b/2
        chord = c_r - (c_r-c_t)/((b-d_ext_fus/2)/2)*span_pos
        x_cg = chord*eval(xstart)+(eval(xend)-eval(xstart))*0.7*chord + l_cabin*0.5 + l_nosecone - 0.25*MAC + cos(np.degrees(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2)))
        w = W_wg/kglbs #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def hortail():
        x_cg = l_fus - (cos(np.radians(sweep_h))*b_h/2 + ct_h) + cos(np.radians(sweep_h))*0.38*b_h/2 + 0.42*MAC_h
        w = W_t/kglbs/4 #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def verttail():
        x_cg = l_fus - 0.58*MAC_v
        w = W_t/kglbs/4*3 #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def engines():
        x_cg = l_cabin*0.5 + l_nosecone - 0.25*MAC + cos(np.degrees(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))) - 0.3*ln
        w = W_pg/kglbs #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def nacelle():
        x_cg = l_cabin*0.5 + l_nosecone - 0.25*MAC + cos(np.degrees(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))) - ln*0.4
        w = W_ng/kglbs #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def mainlandinggear():
        x_cg = x_oew + 2. #CHECK
        w = W_LG/kglbs/8*7 #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def noselandinggear():
        w = W_LG/kglbs/8 #CHANGE
        x_cg = x_oew - (mainlandinggear()[0] - x_oew)*mainlandinggear()[1]/w
        mom = x_cg*w

        return x_cg,w,mom

    x_oew_up = (fus()[2] + wing()[2] + hortail()[2] + verttail()[2] + engines()[2] + nacelle()[2] + mainlandinggear()[2] + noselandinggear()[2])/(fus()[1] + wing()[1] + hortail()[1] + verttail()[1] + engines()[1] + nacelle()[1] + mainlandinggear()[1] + noselandinggear()[1])
    print x_oew_up
    if i == 0:
        x_oew = x_oew_up

#----------------------------------------------FUEL-------------------------------------------------

vols = []

for i in range(len(vol)):
    vols.append(round(vol[i],3))

cgspan = float(vols.index(round(vol[len(vol)-1]/2,3)))/len(vols)*(float(len(vols))/len(b_cur))*b/2

dis1 = cos(np.degrees(lambdac_0))*cgspan

chord = c_r - (c_r-c_t)/((b-d_ext_fus)/2)*cgspan

x_bar_fuel = dis1 + chord*(eval(xstart)+eval(xend))/2

#----------------------------------------------PAYLOAD----------------------------------------------
