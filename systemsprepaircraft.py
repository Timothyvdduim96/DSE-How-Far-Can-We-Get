import matplotlib.pyplot as plt
from Fuselage_Sizing import l_cabin

print(l_cabin)


#parameters

l_nose = 6.17  #distance nose to centerline first door on the right

w_door = 0.69  #door width first door on the right

pitch = 0.79   #pitch seats

x_cargo = 19.0 #position c.g. baggage compartment 

w_cargo = 1000  #weight of aft cargo

w_pax = 2925   #total passenger weight

w_luggage = 574 #luggage weight

w_oe = 11501    #operational empty weight

w_mto = 20000   #maximum take-off weight

n_pax = 37     #number of passengers/seats

MAC = 2.865    #mean aerodynamic chord

X_LEMAC = 12.594 #X-position leading edge mean aerodynamic chord

cg_oew = 12.453  #center of gravity at operational empty weight



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

    l_nose = 6.17  #distance nose to centerline first door on the right

    w_door = 0.69  #door width first door on the right

    pitch = 0.79   #pitch seats

    n_rows = 12    #number of seat rows

    pos_initial = l_nose + w_door/2 #initial position of seats (1st seat)

    positions = []



    for i in range(0,n_rows+1):

        positions.append(pos_initial + pitch*i) 

    

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