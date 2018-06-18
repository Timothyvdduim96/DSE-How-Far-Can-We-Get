from math import *
from wingvol import vol,b_cur,b_frac
import matplotlib.pyplot as plt
#from WingLayout import c_r,c_t,lambdac_0,MAC
import numpy as np
#from Class_II_weight_estimation import *
#from Fuselage_Sizing import *
#from empennage import lh,b_h,sweep_h,ct_h,MAC_h,MAC_v
#from Enginesizing import ln

from parameters import *

l_cockpit = value("l_cockpit")
l_tail = value("l_tail")
l_cabin = 33.7288 #value("l_cabin")
l_fus = 44.1288 #value("l_fus")
MAC = value("MAC")
b = value("b")
c_r = value("c_r")
c_t = value("c_t")
d_ext_fus = 4. #value("d_ext_fus")
xstart = value("x_spar1")
xend = value("x_spar2")
lambdac_0 = value("lambdac_0")
sweep_h = value("sweep_h")
b_h = value("b_h")
ct_h = value("ct_h")
MAC_h = value("MAC_h")
MAC_v = 3.785# value("MAC_v")
ln = 3.25 #value("ln")

x_lemac_lst = []
x_cg_lst = []
frontcglst = []
aftcglst = []

var_x_lemac = np.arange(0.43,0.435,0.001)
aftcg = 1.44

for i in var_x_lemac:
    x_lemac = l_fus*i
    x_lemac_lst.append(i)
    #x_lemac = l_cabin*0.475 + l_cockpit - 0.25*MAC
    l_h = (l_fus - (cos(np.radians(sweep_h))*b_h/2 + ct_h) + cos(np.radians(sweep_h))*0.38*b_h/2 + 0.25*MAC_h) - (x_lemac + 0.25*MAC)

    #------------------------------------------OEW COMPONENTS-------------------------------------------

    def fus():
        x_cg = 0.435*l_fus
        w = value("W_fuselage")
        mom = x_cg*w

        return x_cg,w,mom

    def wing():
        span_pos = 0.35*b/2
        chord = c_r - (c_r-c_t)/((b-d_ext_fus/2)/2)*span_pos
        x_cg = chord*xstart+(xend-xstart)*0.7*chord + x_lemac + tan(np.radians(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2)))
        w = value("W_wing") #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def hortail():
        x_cg = l_fus - (tan(np.radians(sweep_h))*b_h/2 + ct_h) + tan(np.radians(sweep_h))*0.38*b_h/2 + 0.42*MAC_h
        w = value("W_empennage")/4 #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def verttail():
        x_cg = l_fus - 0.58*MAC_v
        w = value("W_empennage")/4*3 #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def engines():
        x_cg = x_lemac + tan(np.radians(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))) - 0.3*ln
        w = value("W_propulsion") #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def nacelle():
        x_cg = x_lemac + tan(np.radians(lambdac_0))*(0.35*(b/2-d_ext_fus/2) - (c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))) - ln*0.4
        w = value("W_nacelle") #ADD
        mom = x_cg*w

        return x_cg,w,mom

    def noselandinggear():
        w = value("W_landinggear")/10. #CHANGE
        x_cg = 4#x_oew - (mainlandinggear()[0] - x_oew)*mainlandinggear()[1]/w
        mom = x_cg*w

        return x_cg,w,mom

    def mainlandinggear():
        x_cg = ((aftcg*MAC + x_lemac) - noselandinggear()[0]*0.06)/0.94 #CHECK
        w = value("W_landinggear")/10.*9. #CHANGE
        mom = x_cg*w

        return x_cg,w,mom

    def fixedequipment ():
        w = value("W_equipment")
        x_cg = 846./866.*0.435*l_fus
        mom = x_cg*w

        return x_cg,w,mom

    x_cg_oew = (fus()[2] + wing()[2] + hortail()[2] + verttail()[2] + engines()[2] + nacelle()[2] + mainlandinggear()[2] + noselandinggear()[2] + fixedequipment ()[2])/(fus()[1] + wing()[1] + hortail()[1] + verttail()[1] + engines()[1] + nacelle()[1] + mainlandinggear()[1] + noselandinggear()[1] + fixedequipment ()[1])
    x_cg_lst.append(x_cg_oew)
    l_cockpit = value("l_cockpit")  #distance nose to centerline first door on the right

    #----------------------------------------------FUEL-------------------------------------------------

    vols = []

    for i in range(len(vol)):
        vols.append(round(vol[i],3))

    cgspan = 5.35972#float(vols.index(round(vol[len(vol)-1]/2,3)))/len(vols)*(float(len(vols))/len(b_cur))*b/2

    dis1 = tan(np.radians(lambdac_0))*cgspan

    chord = c_r - (c_r-c_t)/((b-d_ext_fus/2)/2)*cgspan

    xcg_fuel = dis1 + chord*(xstart+xend)/2 + x_lemac - tan(np.radians(lambdac_0))*(c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2))

    #----------------------------------------------------POTATO-----------------------------------------------------------
    w_door = 1.  #door width first door on the right
    w_toilet = 36*inch_to_cm/100 #from jenkinson
    pitch = value("seat_pitch")*inch_to_cm/100   #pitch seats
    n_pax = 240     #number of passengers/seats
    n_rows = n_pax/6    #number of seat rows
    w_pax = 80*n_pax   #total passenger weight
    w_luggage = 10*n_pax #luggage weight
    w_oe = value("OEW")    #operational empty weight
    w_mto = value("MTOW")   #maximum take-off weight
    w_design_fuel = value("W_fuel")
    w_fuel_mtow = 5000.
    x_cargo = l_fus/2 #position c.g. baggage compartment 
    w_cargo = value("MTOW") - value("OEW") - w_luggage - w_pax - w_fuel_mtow #weight of aft cargo
    MAC = value("MAC")    #mean aerodynamic chord
    row_mid_emergency_exit = n_rows/2
    row_final_emergency_exit = 29

    w_pl = w_pax + w_luggage + w_cargo  #total payload weight
    #w_fuel_mtow = w_mto - (w_oe + w_pl)  #fuel weight at max. payload weight
    w_seat = w_pax/(n_pax) + w_luggage/n_pax  #weight at each seat position
    x_fuel = xcg_fuel   #assumed position c.g. fuel

    X_LEMAC = x_lemac#x_lemac_lst[i]*value("l_fus")#value("x_lemac")           #X-position leading edge mean aerodynamic chord
    cg_oew = x_cg_oew#value("x_cg_oew")  #center of gravity at operational empty weight

    xcolor0 = []
    ycolor0 = []
    xcolor1 = []
    ycolor1 = []
    xcolor2 = []
    ycolor2 = []
    xcolor3 = []
    ycolor3 = []
    xcolor4 = []
    ycolor4 = []
    xcolor5 = []
    ycolor5 = []
    xcolor6 = []
    ycolor6 = []
    xcolor7 = []
    ycolor7 = []
    xcolor8 = []
    ycolor8 = []

    def seatcoordinates():
        pos = l_cockpit + w_door + w_toilet + 0.3 #initial position of seats (1st seat)
        positions = []

        for i in range(n_rows):
            if i == row_mid_emergency_exit:
                row = []
                pos = pos + pitch + 0.20
                positions.append(pos)
            elif i == row_final_emergency_exit:
                row = []
                pos = pos + pitch + 0.80
                positions.append(pos)
            else:
                row = []
                pos = pos + pitch
                positions.append(pos)

        return positions

    seatcoordinates = seatcoordinates()

    #left data points

    xcg = cg_oew
    w = w_oe   #set weight variable
    xbarcg = []   #set list for getting cg positions
    weight = []   #set list for getting weights
    disc_cargo = 1 #number of cargo load points
    xbarcg.append((cg_oew - X_LEMAC)/MAC)  #set initial data point 
    weight.append(w)
    xcolor0.append(xbarcg[0])
    ycolor0.append(weight[0])

    #find cargo data points
    for i in range(0,disc_cargo):
        x_bar_cg = ((xcg*w + x_cargo*w_cargo)/(w + w_cargo) - X_LEMAC)/MAC
        xbarcg.append(((xcg*w + x_cargo*w_cargo)/(w + w_cargo) - X_LEMAC)/MAC)
        xcg = (xcg*w + x_cargo*w_cargo)/(w + w_cargo)
        w += w_cargo
        weight.append(w)
        xcolor1.append(x_bar_cg)
        ycolor1.append(w)

    #find window seats data points
    for i in range(0,len(seatcoordinates)):
        x_bar_cg = ((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC
        xbarcg.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC) 
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat #update the weight
        weight.append(w)
        xcolor2.append(x_bar_cg)
        ycolor2.append(w)

    #find middle seats data points
    for i in range(0,len(seatcoordinates)):
        x_bar_cg = ((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC
        xbarcg.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat   #update the weight
        weight.append(w)
        xcolor3.append(x_bar_cg)
        ycolor3.append(w)

    #find aisle seats data points
    for i in range(0,len(seatcoordinates)):
        x_bar_cg = ((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC
        xbarcg.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat   #update the weight
        weight.append(w)
        xcolor4.append(x_bar_cg)
        ycolor4.append(w)

    
    #find final data point (MTOW)
    xbarcg.append(((xcg*w + x_fuel*w_fuel_mtow)/(w + w_fuel_mtow) - X_LEMAC)/MAC)
    w += w_fuel_mtow   #update the weight
    weight.append(w)
    xcolor5.append(xbarcg[len(xbarcg)-1])
    ycolor5.append(weight[len(weight)-1])

    #right data points

    xcg = cg_oew
    w = w_oe   #set weight variable
    xbarcgr = []   #set list for getting cg positions
    weightr = []   #set list for getting weights
    disc_cargo = 1 #number of cargo load points
    xbarcgr.append((cg_oew - X_LEMAC)/MAC)  #set initial data point 
    weightr.append(w)

    #find cargo data points
    for i in range(0,disc_cargo):
        x_bar_cg = ((xcg*w + x_cargo*w_cargo)/(w + w_cargo) - X_LEMAC)/MAC
        xbarcgr.append(((xcg*w + x_cargo*w_cargo)/(w + w_cargo) - X_LEMAC)/MAC)
        xcg = (xcg*w + x_cargo*w_cargo)/(w + w_cargo)
        w += w_cargo
        weightr.append(w)

    #find window seats data points
    for i in range(0,len(seatcoordinates)):
        i = len(seatcoordinates) - i - 1
        x_bar_cg = ((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC
        xbarcgr.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat #update the weight
        weightr.append(w)
        xcolor6.append(x_bar_cg)
        ycolor6.append(w)

    #find middle seats data points
    for i in range(0,len(seatcoordinates)):
        i = len(seatcoordinates) - i - 1
        x_bar_cg = ((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC
        xbarcgr.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat   #update the weight
        weightr.append(w)
        xcolor7.append(x_bar_cg)
        ycolor7.append(w)

    #find aisle seats data points
    for i in range(0,len(seatcoordinates)):
        i = len(seatcoordinates) - i - 1
        x_bar_cg = ((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC
        xbarcgr.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat   #update the weight
        weightr.append(w)
        xcolor8.append(x_bar_cg)
        ycolor8.append(w)

    frontcg = min(min(xbarcg),min(xbarcgr))
    aftcg = max(max(xbarcg),max(xbarcgr))
    frontcglst.append(frontcg)
    aftcglst.append(aftcg)

#----------------------------------------------SCISSORPLOT----------------------------------------------

SM = 0.05
M = value("M_cr")
A_h = value("Ah")
A = value("A")
c_r = value("c_r")
c_t = value("c_t")
MAC = value("MAC")
d_ext_fus = 4 #value("d_ext_fus")
taper_h = value("ct_h")/value("cr_h")
beta = sqrt(1-M**2)
eta = 0.95
taper = value("taper")
sweep_05_Ch = atan(tan(np.radians(value("sweep_h"))) - (4/A_h)*(0.5*(1-taper_h)/(1+taper_h)))
C_L_alpha_h = 2*pi*A_h/(2 + sqrt(4 + (A_h*beta/eta)**2*(1 + tan(sweep_05_Ch)**2/beta**2)))
S = value("S")
C_L_alpha_w = value("CL_alpha_cruise_clean")
b_f = 4 #value("d_ext_fus")
b = value("b")
l_f = value("l_fus")
S_net = S - d_ext_fus*value("c_r")
C_L_alpha_Ah = C_L_alpha_w*(1 + 2.15*b_f/b)*S_net/S + pi/2*b_f**2/S
r = l_h/(b/2)
m_tv = 0.3                                                          #ROUGH APPROX., CHECK WITH HARRY LATER
lambda_14_w = value("lambdac_4")
def downwash():
    K_eps_lambda = (0.1124 + 0.1265*lambda_14_w + 0.1766*lambda_14_w**2)/r**2 + 0.1024/r + 2
    K_eps_lambda0 = 0.1124/r**2 + 0.1024/r + 2
    downwash = K_eps_lambda/K_eps_lambda0*(r*0.4876/((r**2 + m_tv**2)*sqrt(r**2 + 0.6319 + m_tv**2)) + (1 + (r**2/(r**2 + 0.7915 + 5.0734*m_tv**2))**0.3113)*(1 - sqrt(m_tv**2/(1 + m_tv**2))))*C_L_alpha_w/(pi*A)

    return downwash
downwash = downwash()
#l_h = value("l_h")
c_bar = value("MAC")
V_h_over_V = sqrt(0.85)
C_L_h = -0.8
C_L_Ah = 2.2 #CHANGE, LINK TO PAR FILE
h_f = 4 #value("d_ext_fus")
c_g = S/b
l_fn = x_lemac_lst[3]*l_fus - cos(np.degrees(value("lambdac_0")))*((c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2)))
x_bar_ac_wf = 0.35 - 1.8/C_L_alpha_Ah*b_f*h_f*l_fn/(S*c_bar) + 0.273/(1 + taper)*b_f*c_g*(b - b_f)/(c_bar**2*(b + 2.15*b_f))*tan(lambda_14_w)
l_n = 3.25  #value("l_n")
b_n = 2.334 #CHECK/LINK LATER
k_n = 4.0
x_bar_ac_n = k_n*b_n**2*l_n/(S*c_bar*C_L_alpha_Ah)/2
x_bar_ac = x_bar_ac_wf + x_bar_ac_n
C_L_0 = 0.31
C_m_0_airfoil = -0.114
C_m_ac_w = C_m_0_airfoil*(A*cos(value("lambdac_0"))**2/(A + 2*cos(value("lambdac_0"))))
mu_1 = 0.2
mu_2 = 0.65
mu_3 = 0.057
delta_C_l_max = value("dCL_HLD_land")
c_ratio = value("c_ext_c_land")
S_wf = S + value("S_flaps_land")
C_m_ac_flaps = mu_2*(-mu_1*delta_C_l_max*c_ratio - (C_L_Ah + delta_C_l_max*(1 - S_wf/S))/8*c_ratio*(c_ratio - 1)) + 0.7*A/(1 + 2/A)*mu_3*delta_C_l_max*tan(lambda_14_w) - C_L_Ah*(0.25 - x_bar_ac)
C_m_ac_fus = -1.8*(1 - 2.5*b_f/l_f)*pi*b_f*h_f*l_f/(4*S*c_bar)*C_L_0/C_L_alpha_Ah/value("CL_alpha_low_clean")*C_L_alpha_w
C_m_ac_nac = -0.05
C_m_ac = C_m_ac_w + C_m_ac_flaps + C_m_ac_fus + C_m_ac_nac

x_bar_cg = np.arange(-0.2,1+0.001,0.001)
Sh_S_stab = []
Sh_S_stab_2 = []
Sh_S_cont = []

#---------------------------------STABILITY----------------------------------------
for i in x_bar_cg:
    
    m = (C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)**-1
    q = -(x_bar_ac - SM)/(C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)

    Sh_S_stab.append(m*i + q)

for i in x_bar_cg:
    
    m = (C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)**-1
    q = -(x_bar_ac)/(C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)

    Sh_S_stab_2.append(m*i + q)

#---------------------------------CONTROLLABILITY--------------------------------------

for i in x_bar_cg:
    n = (C_L_h/C_L_Ah*l_h/c_bar*(V_h_over_V)**2)**-1
    p = (C_m_ac/C_L_Ah-x_bar_ac)/(C_L_h/C_L_Ah*l_h/c_bar*(V_h_over_V)**2)

    Sh_S_cont.append(n*i + p)

#-----------------------------------RESULTS--------------------------------------------

Sh_S = 0.13
S_h = Sh_S*S
wingpos = 0.435
x_lemac_pos = wingpos*l_fus
front_bar_cg_final = min(min(xbarcg),min(xbarcgr))
front_cg_final = x_lemac + front_bar_cg_final*MAC
aft_bar_cg_final = max(max(xbarcg),max(xbarcgr))
aft_cg_final = x_lemac + aft_bar_cg_final*MAC
cgrange_final = (aft_bar_cg_final - front_bar_cg_final)*MAC

print "l_h = ", l_h
print "S_h = ", S_h
print "x_lemac = ", x_lemac_pos
print "most fw cg_bar = ", front_bar_cg_final
print "most fw cg = ", front_cg_final
print "most aft cg_bar = ", aft_bar_cg_final
print "most aft cg = ", aft_cg_final
print "cg range = ", cgrange_final


##-----------------------------------PLOTTING----------------------------------------

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

print min(min(xbarcg),min(xbarcgr)), max(max(xbarcg),max(xbarcgr))
#plt.plot(frontcg,x_lemac_lst, color="black", linewidth=5.0)
#plt.plot(aftcg,x_lemac_lst, color="black", linewidth=5.0)
#plt.axis((0,1,min(x_lemac_lst),max(x_lemac_lst)))
#plt.axvline(0.038, linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits")
#plt.axvline(0.44, linestyle = "dashed", linewidth = 1, color = "gray")
plt.plot(xbarcg,weight,xbarcgr,weightr, color="black")
plt.scatter(xcolor0, ycolor0, color="gray", label = "OEW")
plt.scatter(xcolor1, ycolor1, color="blue", label = "Cargo")
plt.scatter(xcolor2, ycolor2, color="red", label = "Window seats")
plt.scatter(xcolor3, ycolor3, color="purple", label = "Middle seats")
plt.scatter(xcolor4, ycolor4, color="orange", label = "Aisle seats")
plt.scatter(xcolor5, ycolor5, color="green", label = "MTOW")
plt.scatter(xcolor6, ycolor6, color="brown", label = "Window seats")
plt.scatter(xcolor7, ycolor7, color="black", label = "Middle seats")
plt.scatter(xcolor8, ycolor8, color="cyan", label = "Aisle seats")

#lines
plt.axhline(w_mto, linestyle = "dashed", color = "cyan", label = "MTOW")
plt.axhline(w_oe + w_pl, linestyle = "dashed", color = "magenta", label = "MZFW")
plt.axhline(w_oe, linestyle = "dashed", color = "orange", label = "OEW")
plt.axvline(min(min(xbarcg),min(xbarcgr)) - 0.02, linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits incl. margin")
plt.axvline(max(max(xbarcg),max(xbarcgr)) + 0.02, linestyle = "dashed", linewidth = 1, color = "gray")
plt.axvline(min(min(xbarcg),min(xbarcgr)), linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits")
plt.axvline(max(max(xbarcg),max(xbarcgr)), linestyle = "dashed", linewidth = 1, color = "gray")
plt.axis((0,1,value("OEW")-1000,value("MTOW")+5000))
#plt.title("Loading diagram")
plt.xlabel("x_cg [%MAC]")
plt.ylabel("Weight [kg]")
ax = plt.subplot(111)
ax.legend(loc="center right", bbox_to_anchor=(1, 0.5))
#plt.show()

##for i in x_lemac_lst:
##    goodyaxis.append(i + 0.0232)
##fig, ax1 = plt.subplots()
##ax1.plot(frontcglst,x_lemac_lst, color="black")
##ax1.plot(aftcglst,x_lemac_lst, color="black")
#####ax1.plot(frontcg,xlemaclst2, color="green")
#####ax1.plot(aftcg,xlemaclst2, color="green")
#####ax1.plot(frontcg,xlemaclst3, color="brown")
#####ax1.plot(aftcg,xlemaclst3, color="brown")
#####ax1.plot(frontcg,xlemaclst4, color="cyan")
#####ax1.plot(aftcg,xlemaclst4, color="cyan")
##ax1.axis((0,1,min(goodyaxis),max(goodyaxis)))
##ax1.set_xlabel('x_cg/MAC')
### Make the y-axis label, ticks and tick labels match the line color.
##ax1.set_ylabel('X_lemac/l_fus', color='b')
##ax1.tick_params('y', colors='b')
####
##ax2 = ax1.twinx()
##ax2.plot(x_bar_cg,Sh_S_cont,label="Controllability")
##ax2.plot(x_bar_cg,Sh_S_stab,label="Stability incl. S.M.")
##ax2.axis((0,1,0,max(max(Sh_S_stab),max(Sh_S_cont))))
##ax2.set_ylabel('S_h/S', color='r')
##ax2.tick_params('y', colors='r')
####
##fig.tight_layout()
##plt.show()

#plt.plot(frontcglst,x_lemac_lst, color="black",linewidth=5)
#plt.plot(aftcglst,x_lemac_lst, color="black",linewidth=5)
#plt.axis((0,1,min(x_lemac_lst),max(x_lemac_lst)))
#plt.plot(x_bar_cg,Sh_S_cont,label="Controllability")
#plt.plot(x_bar_cg,Sh_S_stab,label="Stability incl. S.M.")
#plt.plot(x_bar_cg,Sh_S_stab_2,label="Neutral stability")
#plt.axis((0,max(x_bar_cg),0,max(max(Sh_S_stab),max(Sh_S_cont))))
#ax = plt.subplot(111)
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.xlabel("x_cg/MAC")
#plt.ylabel("Sh/S")
plt.grid()
plt.show()
##plt.plot(frontcglst,x_lemac_lst, color="black")
##plt.plot(aftcglst,x_lemac_lst, color="black")
##plt.axis((0,1,min(x_lemac_lst),max(x_lemac_lst)))
##plt.plot(xbarcg,weight,xbarcgr,weightr, color="black")
##plt.scatter(xcolor0, ycolor0, color="gray", label = "OEW")
##plt.scatter(xcolor1, ycolor1, color="blue", label = "Cargo")
##plt.scatter(xcolor2, ycolor2, color="red", label = "Window seats")
##plt.scatter(xcolor3, ycolor3, color="purple", label = "Middle seats")
##plt.scatter(xcolor4, ycolor4, color="orange", label = "Aisle seats")
##plt.scatter(xcolor5, ycolor5, color="green", label = "MTOW")
##plt.scatter(xcolor6, ycolor6, color="brown", label = "Window seats")
##plt.scatter(xcolor7, ycolor7, color="black", label = "Middle seats")
##plt.scatter(xcolor8, ycolor8, color="cyan", label = "Aisle seats")
##
###lines
##plt.axhline(w_mto, linestyle = "dashed", color = "cyan", label = "MTOW")
##plt.axhline(w_oe + w_pl, linestyle = "dashed", color = "magenta", label = "MZFW")
##plt.axhline(w_oe, linestyle = "dashed", color = "cyan", label = "OEW")
##plt.axvline(min(min(xbarcg),min(xbarcgr)) - 0.02, linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits")
##plt.axvline(max(max(xbarcg),max(xbarcgr)) + 0.02, linestyle = "dashed", linewidth = 1, color = "gray")
##plt.axvline(min(min(xbarcg),min(xbarcgr)), linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits")
##plt.axvline(max(max(xbarcg),max(xbarcgr)), linestyle = "dashed", linewidth = 1, color = "gray")
##plt.axis((-1,0,value("OEW")-1000,value("MTOW")+5000))
##plt.title("Loading diagram")
##plt.xlabel("x_cg [%MAC]")
##plt.ylabel("Weight [kg]")
##ax = plt.subplot(111)
##ax.legend(loc="center right", bbox_to_anchor=(1, 0.5))
##plt.show()

string_mergedstabcont = ["Sh_S", "S_h", "wingpos", "x_lemac_pos", "front_bar_cg_final", "front_cg_final", "aft_bar_cg_final", "aft_cg_final", "cgrange_final"]
