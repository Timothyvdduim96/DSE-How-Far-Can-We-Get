# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:14:03 2018

@author: Bart Jacobson
"""

import matplotlib.pyplot as plt
from parameters import *

#parameters
l_cockpit = value("l_cockpit")  #distance nose to centerline first door on the right
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
w_fuel_mtow = 1000.
x_cargo = 20.0 #position c.g. baggage compartment 
w_cargo = value("MTOW") - value("OEW") - w_luggage - w_pax - w_fuel_mtow #weight of aft cargo
MAC = value("MAC")    #mean aerodynamic chord
X_LEMAC = value("x_lemac")          #value("x_lemac") #X-position leading edge mean aerodynamic chord
cg_oew = value("x_cg_oew")  #center of gravity at operational empty weight
row_mid_emergency_exit = n_rows/2
row_final_emergency_exit = 29

w_pl = w_pax + w_luggage + w_cargo  #total payload weight
#w_fuel_mtow = w_mto - (w_oe + w_pl)  #fuel weight at max. payload weight
w_seat = w_pax/(n_pax) + w_luggage/n_pax  #weight at each seat position
x_fuel = value("xcg_fuel")   #assumed position c.g. fuel

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
cgrange_mac = aftcg - frontcg
cgrange = cgrange_mac*value("MAC")
print cgrange_mac,cgrange
print frontcg
print aftcg

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
plt.axhline(w_oe, linestyle = "dashed", color = "cyan", label = "OEW")
plt.axvline(min(min(xbarcg),min(xbarcgr)) - 0.02, linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits")
plt.axvline(max(max(xbarcg),max(xbarcgr)) + 0.02, linestyle = "dashed", linewidth = 1, color = "gray")
plt.axvline(min(min(xbarcg),min(xbarcgr)), linestyle = "dashed", linewidth = 1, color = "gray", label = "c.g. limits")
plt.axvline(max(max(xbarcg),max(xbarcgr)), linestyle = "dashed", linewidth = 1, color = "gray")
plt.axis((0,1,value("OEW")-1000,value("MTOW")+5000))
plt.title("Loading diagram")
plt.xlabel("x_cg [%MAC]")
plt.ylabel("Weight [kg]")
ax = plt.subplot(111)
ax.legend(loc="center right", bbox_to_anchor=(1, 0.5))
plt.show()

string_loadingdiagram = ["frontcg","aftcg","cgrange_mac","cgrange"]