from math import *
from wingvol import a,xstart,xend,c_r_f,c_t_f,b,vol,b_cur,d_ext_fus
from WingLayout import c_r,c_t,lambdac_0
import numpy as np

#S_1 = a*c_r_f**2
#S_2 = a*c_t_f**2

#alpha = b/4*(S_1+3*S_2+2*sqrt(S_1*S_2))/(4*(S_1+S_2+sqrt(S_1*S_2)))

#dis = np.radians(alpha)*b/4

vols = []

for i in range(len(vol)):
    vols.append(round(vol[i],3))

cgspan = float(vols.index(round(vol[len(vol)-1]/2,3)))/len(vols)*(float(len(vols))/len(b_cur))*b/2

dis1 = cos(np.degrees(lambdac_0))*cgspan

chord = c_r - (c_r-c_t)/((b-d_ext_fus)/2)*cgspan

x_bar_fuel = dis1 + chord*(eval(xstart)+eval(xend))/2
