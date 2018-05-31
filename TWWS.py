from math import *
import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------------parameters--------------------------------------------------
xsize = 11000
s_l = 2000
V_land = sqrt(s_l/0.5847)
gr = 9.80665
n_max = 2.5 #change
rho = 1.167
rho_0 = 1.2255
rho_cruise = 0.310828 #at 12 km altitude
T = 216.650

#------------------------------------design specific parameters---------------------------------------------

designdatalst = 'dop.csv'

designdata = np.genfromtxt(designdatalst, dtype='string', delimiter=';')

ch = raw_input("choose your design nr (1 to 6): ")

C_L_max_1 = eval(designdata[1][ch]) 
C_L_max_2 = eval(designdata[2][ch]) 
C_L_max_3 = eval(designdata[3][ch]) 
C_L_clean_1 = eval(designdata[4][ch]) 
C_L_clean_2 = eval(designdata[5][ch]) 
C_L_clean_3 = eval(designdata[6][ch])
C_L_TO_1 = eval(designdata[7][ch]) 
C_L_TO_2 = eval(designdata[8][ch])
C_L_TO_3 = eval(designdata[9][ch])
C_D_0 = eval(designdata[19][ch]) 
V_max = eval(designdata[10][ch]) 
f = 0.9745 
V_s = eval(designdata[11][ch]) 
cV = 0.024
A = eval(designdata[12][ch]) 
#A_2 = eval(designdata[13][ch]) 
#A_3 = eval(designdata[14][ch]) 
e = 0.85 
c = 17 #change
TOP = eval(designdata[15][ch])
V = V_s
MTOW = eval(designdata[16][ch])
eff = eval(designdata[17][ch])

#land limit

def land_limit(rho,C_L_max_1,C_L_max_2,C_L_max_3,V_land,f):

    WS_1 = (0.5*rho*C_L_max_1*V_land**2)/f
    WS_2 = (0.5*rho*C_L_max_2*V_land**2)/f
    WS_3 = (0.5*rho*C_L_max_3*V_land**2)/f

    return WS_1,WS_2,WS_3

#cruise flight limit

def cruise_limit(rho_cruise,C_L_clean_1,C_L_clean_2,C_L_clean_3,V_s):

    WS_1 = 0.5*rho_cruise*C_L_clean_1*V_s**2
    WS_2 = 0.5*rho_cruise*C_L_clean_2*V_s**2
    WS_3 = 0.5*rho_cruise*C_L_clean_3*V_s**2

    return WS_1,WS_2,WS_3

#climb gradient limit

def climb_gradient(cV,C_D_0,A,e):

    C_D_0 = 1.05*(C_D_0 + 0.015)
    e = e + 0.05

    factor = 2 #one engine inoperative (CS25)
    TW_1 = factor*(cV + 2*sqrt(C_D_0/(pi*A*e)))
    #TW_2 = factor*(cV + 2*sqrt(C_D_0/(pi*A_2*e)))
    #TW_3 = factor*(cV + 2*sqrt(C_D_0/(pi*A_3*e)))

    return TW_1

#climb rate limit

def climb_rate(c,rho,C_D_0,A,e,xsize):

    C_D = 4*C_D_0
    C_L_1 = sqrt(3*C_D_0*pi*A*e)
    #C_L_2 = sqrt(3*C_D_0*pi*A_2*e)
    #C_L_3 = sqrt(3*C_D_0*pi*A_3*e)

    TW_1 = []
    TW_2 = []
    TW_3 = []

    WS = np.arange(1,xsize)
    
    for i in range(len(WS)):
    
        TW_1.append(c/(sqrt(2*WS[i]/(rho*C_L_1))) + C_D/C_L_1)
        #TW_2.append(c/(sqrt(2*WS[i]/(rho*C_L_2))) + C_D/C_L_2)
        #TW_3.append(c/(sqrt(2*WS[i]/(rho*C_L_3))) + C_D/C_L_3)

    return WS,TW_1

#take-off limit

def take_off(TOP,C_L_TO_1,C_L_TO_2,C_L_TO_3,rho,rho_0):

    sigma = 1#rho/rho_0

    TW_1 = []
    TW_2 = []
    TW_3 = []

    WS = np.arange(1,xsize)
    
    for i in range(len(WS)):
    
        TW_1.append(WS[i]/(TOP*C_L_TO_1*sigma))
        TW_2.append(WS[i]/(TOP*C_L_TO_2*sigma))
        TW_3.append(WS[i]/(TOP*C_L_TO_3*sigma))

    return TW_1,TW_2,TW_3

#max speed limit

def speed_limit(C_D_0,rho_cruise,V_max,A,e):

    TW_1 = []
    #TW_2 = []
    #TW_3 = []

    WS = np.arange(1,xsize)
    
    for i in range(len(WS)):
    
        TW_1.append(0.8/0.9*(1.225/rho_cruise)**0.75*((C_D_0*rho_cruise*0.5*V_max**2)/(0.8*WS[i]) + (0.8*WS[i])/(pi*A*e*0.5*rho_cruise*V_max**2)))
        #TW_2.append(0.8/0.9*(1.225/rho_cruise)**0.75*((C_D_0*rho_cruise*0.5*V_max**2)/(0.8*WS[i]) + (0.8*WS[i])/(pi*A_2*e*0.5*rho_cruise*V_max**2)))
        #TW_3.append(0.8/0.9*(1.225/rho_cruise)**0.75*((C_D_0*rho_cruise*0.5*V_max**2)/(0.8*WS[i]) + (0.8*WS[i])/(pi*A_3*e*0.5*rho_cruise*V_max**2)))

    return TW_1

def loadfactor_limit(C_D_0,rho_cruise,V,n_max,A):

    n_max = n_max + 0.1 #safety factor
    TW_1 = []
    #TW_2 = []
    #TW_3 = []

    WS = np.arange(1,xsize)
    
    for i in range(len(WS)):
    
        TW_1.append(C_D_0*0.5*rho_cruise*V**2/WS[i]+WS[i]*n_max**2/(pi*A*e*0.5*rho_cruise*V**2))
        #TW_2.append(C_D_0*0.5*rho_cruise*V**2/WS[i]+WS[i]*n_max**2/(pi*A_2*e*0.5*rho_cruise*V**2))
        #TW_3.append(C_D_0*0.5*rho_cruise*V**2/WS[i]+WS[i]*n_max**2/(pi*A_3*e*0.5*rho_cruise*V**2))

    return TW_1

WS = np.arange(1,xsize)

speedform = ['%.4f' % elem for elem in climb_rate(c,rho,C_D_0,A,e,xsize)[1]]
toform = ['%.4f' % elem for elem in take_off(TOP,C_L_TO_1,C_L_TO_2,C_L_TO_3,rho,rho_0)[2]]

xstart = []
ystart = []
xend = []
yend = []

for i in range(len(WS)):
    if speedform[i] == toform[i]:
        xstart.append(i)
        ystart.append(speedform[i])

for i in range(len(WS)):
    if i == round(land_limit(rho,C_L_max_1,C_L_max_2,C_L_max_3,V_land,f)[2]):
        xend.append(i)
        yend.append(toform[i])

#equation design point
##MTOW = 66904
##s = 0. #define desired surface area
##if s > 0.:
##    x = MTOW*9.81/s
##else:
##    x = 7150.    #define design W/S
##y = (eval(yend[0])-eval(ystart[0]))/(xend[0]-xstart[0])*x + (eval(ystart[0]) - xstart[0]*(eval(yend[0])-eval(ystart[0]))/(xend[0]-xstart[0]))
##
##print("The surface area is", round(MTOW*9.81/x,2), "m^2")
##print("The thrust is", round(MTOW*9.81*y/1000,2), "kN")
##b=[[x,y]]
##plt.plot(*zip(*b), marker='o', color='olive', label="design point")
##z=[[xstart[0]+30,eval(ystart[0])+0.002]]
##plt.plot(*zip(*z), marker='o', color='olive')

##font = {'family' : 'normal',
##        'weight' : 'normal',
##        'size'   : 14}
##
##plt.rc('font', **font)

#plotting
landlimit_1 = land_limit(rho,C_L_max_1,C_L_max_2,C_L_max_3,V_land,f)[0]
landlimit_2 = land_limit(rho,C_L_max_1,C_L_max_2,C_L_max_3,V_land,f)[1]
landlimit_3 = land_limit(rho,C_L_max_1,C_L_max_2,C_L_max_3,V_land,f)[2]
plt.axvline(landlimit_1, linestyle="dashed", color="Red",label="Landing with CL=2.0")
plt.axvline(landlimit_2, linestyle="dotted", color="Red",label="Landing with CL=2.2")
plt.axvline(landlimit_3, linestyle="solid", color="Red",label="Landing with CL=3.0")

cruiselimit_1 = cruise_limit(rho,C_L_clean_1,C_L_clean_2,C_L_clean_3,V_s)[0]
cruiselimit_2 = cruise_limit(rho,C_L_clean_1,C_L_clean_2,C_L_clean_3,V_s)[1]
cruiselimit_3 = cruise_limit(rho,C_L_clean_1,C_L_clean_2,C_L_clean_3,V_s)[2]
plt.axvline(cruiselimit_1, linestyle="dashed", color="Blue",label="Cruising with CL=1.0")
plt.axvline(cruiselimit_2, linestyle="dotted", color="Blue",label="Cruising with CL=1.2")
plt.axvline(cruiselimit_3, linestyle="solid", color="Blue",label="Cruising with CL=1.4")

climbgradientlimit_1 = climb_gradient(cV,C_D_0,A,e)
#climbgradientlimit_2 = climb_gradient(cV,C_D_0,A,A_2,A_3,e)[1]
#climbgradientlimit_3 = climb_gradient(cV,C_D_0,A,A_2,A_3,e)[2]
plt.axhline(climbgradientlimit_1, linestyle="solid", color="Green",label="Climb gradient with A=10.5")
#plt.axhline(climbgradientlimit_2, linestyle="dotted", color="Green",label="Climb gradient with A=12")
#plt.axhline(climbgradientlimit_3, linestyle="solid", color="Green",label="Climb gradient with A=13")

xaxis = climb_rate(c,rho,C_D_0,A,e,xsize)[0]
climbratelimit_1 = climb_rate(c,rho,C_D_0,A,e,xsize)[1]
#climbratelimit_2 = climb_rate(c,rho,C_D_0,A,A_2,A_3,e,xsize)[2]
#climbratelimit_3 = climb_rate(c,rho,C_D_0,A,A_2,A_3,e,xsize)[3]
plt.plot(xaxis, climbratelimit_1, linestyle="solid", color="Black",label="Climb rate with A=10.5")
#plt.plot(xaxis, climbratelimit_2, linestyle="dotted", color="Black",label="Climb rate with A=12")
#plt.plot(xaxis, climbratelimit_3, linestyle="solid", color="Black",label="Climb rate with A=13")

takeofflimit_1 = take_off(TOP,C_L_TO_1,C_L_TO_2,C_L_TO_3,rho,rho_0)[0]
takeofflimit_2 = take_off(TOP,C_L_TO_1,C_L_TO_2,C_L_TO_3,rho,rho_0)[1]
takeofflimit_3 = take_off(TOP,C_L_TO_1,C_L_TO_2,C_L_TO_3,rho,rho_0)[2]
plt.plot(xaxis, takeofflimit_1, linestyle="dashed", color="Cyan",label="Taking off with CL=2.0")
#plt.plot(xaxis, takeofflimit_2, linestyle="dotted", color="Cyan",label="Taking off with CL=2.5")
plt.plot(xaxis, takeofflimit_3, linestyle="solid", color="Cyan",label="Taking off with CL=3.0")

maxspeedlimit_1 = speed_limit(C_D_0,rho_cruise,V_max,A,e)
#maxspeedlimit_2 = speed_limit(C_D_0,rho_cruise,V_max,A,A_2,A_3,e)[1]
#maxspeedlimit_3 = speed_limit(C_D_0,rho_cruise,V_max,A,A_2,A_3,e)[2]
plt.plot(xaxis, maxspeedlimit_1, linestyle="solid", color="Violet",label="Max speed with A=10.5")
#plt.plot(xaxis, maxspeedlimit_2, linestyle="dotted", color="Violet",label="Max speed with A=12")
#plt.plot(xaxis, maxspeedlimit_3, linestyle="solid", color="Violet",label="Max speed with A=13")

loadfactorlimit_1 = loadfactor_limit(C_D_0,rho,V,n_max,A)
#loadfactorlimit_2 = loadfactor_limit(C_D_0,rho,V,n_max,A,A_2,A_3)[1]
#loadfactorlimit_3 = loadfactor_limit(C_D_0,rho,V,n_max,A,A_2,A_3)[2]
plt.plot(xaxis, loadfactorlimit_1, linestyle="solid", color="Maroon",label="Load factor with A=10.5")
#plt.plot(xaxis, loadfactorlimit_2, linestyle="dotted", color="Maroon",label="Load factor with A=12")
#plt.plot(xaxis, loadfactorlimit_3, linestyle="solid", color="Maroon",label="Load factor with A=13")

a=[[7457,0.32]]
plt.plot(*zip(*a), marker='o', markersize=8, color='fuchsia', label="reference aircraft") #A321neo
##b=[[6239,0.35]]
##plt.plot(*zip(*b), marker='o', color='olive')
##c=[[5000,0.28]]
##plt.plot(*zip(*c), marker='o', color='olive')
d=[[7130.6,0.3253]]
plt.plot(*zip(*d), marker='o', markersize=8, color='fuchsia')#, label="A321-200") #A321-200
e=[[5888.8,0.3084]]
plt.plot(*zip(*e), marker='o', markersize=8, color='fuchsia')#, label="A320-200") #A320-200
f=[[6703.2,0.291]]
plt.plot(*zip(*f), marker='o', markersize=8, color='fuchsia')#, label="B737-900") #B737-900
g=[[6251.5,0.358]]
plt.plot(*zip(*g), marker='o', markersize=8, color='fuchsia')#, label="A320neo") #A320neo
h=[[6819.4,0.326]]
plt.plot(*zip(*h), marker='o', markersize=8, color='fuchsia')#, label="B737-MAX9") #B737-MAX9
i=[[6219,0.2789]]
plt.plot(*zip(*i), marker='o', markersize=8, color='fuchsia')#, label="737-800") #B737-800
j=[[6346.6,0.3114]]
plt.plot(*zip(*j), marker='o', markersize=8, color='fuchsia')#, label="B737 MAX8") #B737 MAX8
k=[[5515.6,0.2615]]
plt.plot(*zip(*k), marker='o', markersize=8, color='fuchsia')#, label="737-700") #B737-700
l=[[6199.5,0.3188]]
plt.plot(*zip(*l), marker='o', markersize=8, color='fuchsia')#, label="B737 MAX7") #B737 MAX7
m=[[5901.9,0.2818]]
plt.plot(*zip(*m), marker='o', markersize=8, color='fuchsia')#, label="Bombardier CS300") #Bombardier CS300
n=[[5302.,0.325]]
plt.plot(*zip(*n), marker='v', markersize=8, color='black',label="design point")#, label="Bombardier CS300") #Bombardier CS300

#plt.title("Pressure ratio")

plt.xlabel("W/S")
plt.ylabel("T/W")
ax = plt.subplot(111)
plt.axis((0,xsize,0, 0.35))
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()
plt.show()

DPx = raw_input("Fill in a x-coordinate of a design point: ")
DPy = raw_input("Fill in a y-coordinate of a design point: ")
A = raw_input("Fill in your chosen aspect ratio: ")
DP = []
DP.append(DPx)
DP.append(DPy)
S = round(MTOW*gr/eval(DPx),2)
T = round(MTOW*gr*eval(DPy)/1000)
print "Wing area = ", S, "m^2"
print "Thrust = ", T, "kN"

DPx = eval(DPx)
DPy = eval(DPy)
A = eval(A)

def findclcruise(DPx,cruiselimit_1,cruiselimit_2,cruiselimit_3,C_L_clean_1,C_L_clean_2,C_L_clean_3):

    if DPx < cruiselimit_1:
        C_Lcr = round((DPx/cruiselimit_1*C_L_clean_1),2)
    elif DPx >= cruiselimit_1 and DPx <= cruiselimit_2:
        C_Lcr = round(((DPx-cruiselimit_1)/(cruiselimit_2-cruiselimit_1)*(C_L_clean_2-C_L_clean_1)+C_L_clean_1),2)
    elif DPx > cruiselimit_2 and DPx <= cruiselimit_3:
        C_Lcr = round(((DPx-cruiselimit_2)/(cruiselimit_3-cruiselimit_2)*(C_L_clean_3-C_L_clean_2)+C_L_clean_2),2)
    else:
        C_Lcr = "Cruise requirement not satisfied"

    return C_Lcr

C_Lcr = findclcruise(DPx,cruiselimit_1,cruiselimit_2,cruiselimit_3,C_L_clean_1,C_L_clean_2,C_L_clean_3)

to1 = takeofflimit_1[int(DPx)]
to2 = takeofflimit_2[int(DPx)]
to3 = takeofflimit_3[int(DPx)]

def findclto(DPy,to1,to2,to3,C_L_TO_1,C_L_TO_2):
    
    if DPy >= to1:
        C_Lto = C_L_TO_1
    elif DPy < to1 and DPy >= to2:
        C_Lto = round((to1-DPy)/(to1-to2)*(C_L_TO_2 - C_L_TO_1)+C_L_TO_1,2)
    elif DPy < to2 and DPy >= to3:
        C_Lto = round((to2-DPy)/(to2-to3)*(C_L_TO_3 - C_L_TO_2)+C_L_TO_2,2)
    else:
        C_Lto = "Take off requirement not satisfied"

    return C_Lto

def findcland(DPx,landlimit_1,landlimit_2,landlimit_3,C_L_max_1,C_L_max_2,C_L_max_3):

    if DPx < landlimit_1:
        C_Lland = round((DPx/landlimit_1*C_L_max_1),2)
    elif DPx >= landlimit_1 and DPx <= landlimit_2:
        C_Lland = round(((DPx-landlimit_1)/(landlimit_2-landlimit_1)*(C_L_max_2-C_L_max_1)+C_L_max_1),2)
    elif DPx > landlimit_2 and DPx <= landlimit_3:
        C_Lland = round(((DPx-landlimit_2)/(landlimit_3-landlimit_2)*(C_L_max_3-C_L_max_2)+C_L_max_2),2)
    else:
        C_Lland = "Landing requirement not satisfied"

    return C_Lland

C_Lland = findcland(DPx,landlimit_1,landlimit_2,landlimit_3,C_L_max_1,C_L_max_2,C_L_max_3)

print 'C_L_max_cruise = ', findclcruise(DPx,cruiselimit_1,cruiselimit_2,cruiselimit_3,C_L_clean_1,C_L_clean_2,C_L_clean_3)
print "C_L_max_land = ", findcland(DPx,landlimit_1,landlimit_2,landlimit_3,C_L_max_1,C_L_max_2,C_L_max_3)
print "C_L_max_takeoff = ", findclto(DPy,to1,to2,to3,C_L_TO_1,C_L_TO_2)

    
