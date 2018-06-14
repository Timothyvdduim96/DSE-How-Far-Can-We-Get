#Fuselage Sizing Program -------------- Development by Patrik Kovacik Copyright :D
from math import *
from parameters import *

#B: Boeing 737-700 value Single Class highest density
#A: Airbus A320neo,A321neo value Single Class highest density

#Input Parameters

    #Width
N_aisle=1
w_seat=17 # [inch] B:17 A:17/18
w_aisle=20 # [inch] B:20 A:19/25
sidewall_clearance=2 #[cm]
seat_corr=1.129 #Correction for armrests of seat B:1.356/3 A:1.129/3

    #Height
h_floor=1.378  #[m]  B:1.12 A:1.23,1.24
t_floor=110 #[mm] A:108
h_headspace=63 #[inch] B: 62.2, A: 64
h_aisle=86.3 #[inch] B:86.3
h_luggage=h_aisle-h_headspace #[inch] Maximal size of luggage from top of fuselage
h_extra=0 #[mm] Place for fit other things 
h_cabin = 2.192 #[m]
h_cargo = 1.195 #[m]
    #Length
seat_pitch=28 # [inch] B:30 A:28/29 Adsee 32
N_seat_row=6 # [seat/row]  B:6 A:6
l_cockpit=4 #[meters]
ratio_tail=1.6  #[length/diameter fus] 1.0-2.0

    #Other
N_passengers=240 #[-] B:184 A:180,220      WARNING!!! MUST BE MULTIPLE OF SIX!!!!
ext_int_corr=1.088
N_rows_A321neo = 41
l_cabin_A321neo = 34.44


#Output
N_rows=N_passengers/N_seat_row
w_floor= 3.61 #Internal Width of Floor [m]
w_cargo = 1.6 #[m]

d_int_fus= 3.68 #Chossing the diameter such that both width and height conditions are satisfied
d_ext_fus= 4.0
r_int_fus=d_int_fus*0.5 #Radius 
r_ext_fus= 2.0 #[m] External Radius

l_seats_A321neo=N_rows_A321neo*seat_pitch*inch_to_m # [meters] Length of seating area
l_seats = N_rows*seat_pitch*inch_to_m
restcabinspace = l_cabin_A321neo -l_seats_A321neo

l_cabin = l_seats+restcabinspace 


ratio_nosecone=1.5 #1.0-2.0 Conventional Aircraft Design (drive)
ratio_tailcone=3.0 #2.0-3.0 
l_nosecone=d_ext_fus*ratio_nosecone #[m] Length of nosecone
l_tailcone=d_ext_fus*ratio_tailcone #[m] Length of tailcone
l_tail=d_ext_fus*ratio_tail

l_fus = l_cockpit+l_cabin+l_tail 
F=l_fus/(2*r_ext_fus) #Fineness Ratio

theta=2*asin(w_floor/(2*r_int_fus))
area_cargo= 2.849 #[m^2] Area available for Cargo excluding support
area_int_fus=pi*r_int_fus**2
area_ext_fus=pi*r_ext_fus**2 #[m^2] Entire Internal Frontal Area
area_cabin=area_int_fus-area_cargo-0.11*3.61 #[m^2] Area in cabin 

print "Length of the fuselage is",round(l_fus,2)," m"
print "Length of the cabin is",round(l_cabin,2)," m"
print "Diameter of the fuselage is",round(d_int_fus,2)," m"
print "Width of the floor is",round(w_floor,2)," m"
print "Height of the floor is",h_floor,"m"

string_Fuselage_Sizing=["h_cabin","h_cargo","w_cargo","N_aisle","w_seat","w_aisle","sidewall_clearance","seat_corr","h_floor","t_floor","h_headspace","h_aisle","h_luggage","h_extra","seat_pitch","N_seat_row","l_cockpit","ratio_tail","N_passengers","ext_int_corr","N_rows","w_floor","d_int_fus","d_ext_fus","r_int_fus","r_ext_fus","l_seats","l_cabin","ratio_nosecone","ratio_tailcone","l_nosecone","l_tailcone","l_fus","F","area_cargo","area_cabin","area_ext_fus","l_tail"]






