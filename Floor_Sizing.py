#Floor Sizing

from Fuselage_Sizing import *
import matplotlib.pyplot as plt


#Define Weights
W_passenger=90 #kg
W_seat=5 #kg


W_pax=N_passengers*W_passenger
W_seats=W_seat*N_passengers



#Define Floor Geometry

def Cbeam(b,h,t,dis):
    A=t*(b+h)
    cg=b/2.0
    I=(1/12.0)*h**3*t+A*(dis-cg)**2    
    return A,I


    #C-beam
b_str_1=50 #mm
h_str_1=100 #mm
t_str_1=10 #mm
t_skin_floor=10 #mm
[A_str_1,I_str_1]=Cbeam(b_str_1,h_str_1,t_str_1,b_str_1/2+t_str_1)


b_str_2=50 #mm
h_str_2=100 #mm
t_str_2=10 #mm
L_str_2=0.87 #m
[A_str_2,I_str_2]=Cbeam(b_str_2,h_str_2,t_str_2,0)







    




