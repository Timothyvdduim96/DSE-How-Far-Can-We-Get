import matplotlib.pyplot as plt
from parameters import *

#parameters
l_cockpit = value("l_cockpit")  #distance nose to centerline first door on the right
w_door = 1.  #door width first door on the right
w_toilet = 36*inch_to_cm/100 #from jenkinson
pitch = value("seat_pitch")*inch_to_cm/100   #pitch seats
n_pax = 240     #number of passengers/seats
n_rows = 40    #number of seat rows
w_pax = 80*n_pax   #total passenger weight
w_luggage = 10*n_pax #luggage weight
w_oe = value("OEW")    #operational empty weight
w_mto = value("MTOW")   #maximum take-off weight
w_design_fuel = value("W_fuel")
x_cargo = 19.0 #position c.g. baggage compartment 
w_cargo = value("MTOW") - value("OEW") - w_luggage - w_pax  #weight of aft cargo
MAC = value("MAC")    #mean aerodynamic chord
X_LEMAC = value("x_lemac") #X-position leading edge mean aerodynamic chord
cg_oew = value("xcg_oew")  #center of gravity at operational empty weight
row_mid_emergency_exit = n_rows/2
row_final_emergency_exit = 29

w_pl = w_pax + w_luggage + w_cargo  #total payload weight
w_fuelatmaxpayload = w_mto - (w_oe + w_pl)  #fuel weight at max. payload weight
w_seat = w_pax/(n_pax) + w_luggage/n_pax  #weight at each seat position
x_fuel = X_LEMAC + MAC/2   #assumed position c.g. fuel

xcolor1 = []
ycolor1 = []
xcolor2 = []
ycolor2 = []
xcolor3 = []
ycolor3 = []

def seatcoordinates():
    pos = l_cockpit + w_door + w_toilet + 0.3 #initial position of seats (1st seat)
    positions = []

    for i in range(n_rows):
        if i == row_mid_emergency_exit:
            row = []
            pos = pos + pitch + 0.20
            for j in range(6):
                row.append(pos)
            positions.append(row)
        elif i == row_final_emergency_exit:
            row = []
            pos = pos + pitch + 0.80
            for j in range(6):
                row.append(pos)
            positions.append(row)
        else:
            row = []
            pos = pos + pitch
            for j in range(6):
                row.append(pos)
            positions.append(row)
    
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

#find cargo data points
for i in range(0,disc_cargo):
    xbarcg.append(((xcg*w + x_cargo*w_cargo)/(w + w_cargo) - X_LEMAC)/MAC)
    xcg = (xcg*w + x_cargo*w_cargo)/(w + w_cargo)
    w += w_cargo
    weight.append(w)
    xcolor1.append(xbarcg[i])
    ycolor1.append(weight[i])

#find window seats data points
for i in range(0,len(seatcoordinates)):
    #print(xcg)
    if i == 0: 
        xbarcg.append(((xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat)  #find the new cg
        w += w_seat   #update the weight
        weight.append(w)
        xcolor2.append(xbarcg[i])
        ycolor2.append(weight[i])
    else:
        xbarcg.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat #update the weight
        weight.append(w)
        xcolor2.append(xbarcg[i])
        ycolor2.append(weight[i])

#find aisle seats data points
for i in range(1,len(seatcoordinates)):
    xbarcg.append(((xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat) - X_LEMAC)/MAC)
    xcg = (xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat)  #find the new cg
    w += w_seat   #update the weight
    weight.append(w)
    xcolor3 = []
    ycolor3 = []

#find final data point (MTOW)
xbarcg.append(((xcg*w + x_fuel*w_fuelatmaxpayload)/(w + w_fuelatmaxpayload) - X_LEMAC)/MAC)
w += w_fuelatmaxpayload   #update the weight
weight.append(w)


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
    xbarcgr.append(((xcg*w + x_cargo*w_cargo)/(w + w_cargo) - X_LEMAC)/MAC)
    xcg = (xcg*w + x_cargo*w_cargo)/(w + w_cargo)
    w += w_cargo
    weightr.append(w)

#find window seats data points
for i in range(0,len(seatcoordinates)):
    i = len(seatcoordinates) - i - 1
    #print(xcg)
    if i == 0: 
        xbarcgr.append(((xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat)  #find the new cg
        w += w_seat   #update the weight
        weightr.append(w)
    else:
        xbarcgr.append(((xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2) - X_LEMAC)/MAC)
        xcg = (xcg*w + seatcoordinates[i]*w_seat*2)/(w + w_seat*2)  #find the new cg
        w += 2*w_seat #update the weight
        weightr.append(w)

#find aisle seats data points
for i in range(1,len(seatcoordinates)):
    i = len(seatcoordinates) - i 
    xbarcgr.append(((xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat) - X_LEMAC)/MAC)
    xcg = (xcg*w + seatcoordinates[i]*w_seat)/(w + w_seat)  #find the new cg
    w += w_seat   #update the weight
    weightr.append(w)

print(xbarcg)
print(weight)

#plotting

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

for i in range(len(xbarcg)):
    if i < disc_cargo:
        xcolor0.append(xbarcg[i])
        ycolor0.append(weight[i])
    elif i == disc_cargo:
        xcolor1.append(xbarcg[i])
        ycolor1.append(weight[i])
    elif disc_cargo <= i <= len(seatcoordinates) + 1:
        xcolor2.append(xbarcg[i])
        ycolor2.append(weight[i])
        xcolor5.append(xbarcgr[i])
        ycolor5.append(weightr[i])
    elif len(seatcoordinates) + 1 < i <= 2*len(seatcoordinates):
        xcolor3.append(xbarcg[i])
        ycolor3.append(weight[i])
        xcolor6.append(xbarcgr[i])
        ycolor6.append(weightr[i])
    else:
        xcolor4.append(xbarcg[i])
        ycolor4.append(weight[i])

plt.plot(xbarcg,weight,xbarcgr,weightr, color="black")
plt.scatter(xcolor0, ycolor0, color="gray", label = "OEW")
plt.scatter(xcolor1, ycolor1, color="blue", label = "Cargo")
plt.scatter(xcolor2, ycolor2, color="red", label = "Window seats")
plt.scatter(xcolor3, ycolor3, color="purple", label = "Aisle seats")
plt.scatter(xcolor4, ycolor4, color="orange", label = "MTOW")
plt.scatter(xcolor5, ycolor5, color="green", label = "Window seats")
plt.scatter(xcolor6, ycolor6, color="brown", label = "Aisle seats")

#lines
plt.axhline(w_mto, linestyle = "dashed", color = "cyan", label = "MTOW")
plt.axhline(w_oe + w_pl, linestyle = "dashed", color = "magenta", label = "MZFW")
plt.axhline(w_oe, linestyle = "dashed", color = "yellow", label = "OEW")
plt.axvline(min(min(xbarcg),min(xbarcgr)) - 0.02, linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits")
plt.axvline(max(max(xbarcg),max(xbarcgr)) + 0.02, linestyle = "dashed", linewidth = 1, color = "gray")
plt.title("Loading diagram")
plt.xlabel("x_cg [%MAC]")
plt.ylabel("Weight [kg]")
ax = plt.subplot(111)
ax.legend(loc="center right", bbox_to_anchor=(1, 0.5))
plt.show()
