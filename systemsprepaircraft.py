# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 09:44:02 2018

<<<<<<< HEAD
@author: Bart Jacobson
"""
=======
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
>>>>>>> 5ff575fde8319f865e03bcc353fbe467a041154e

