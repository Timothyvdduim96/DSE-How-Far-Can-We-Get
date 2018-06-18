# -*- coding: utf-8 -*-
"""
Created on Fri Jun 08 09:11:17 2018

@author: helua
"""
from math import * 

rho_0 = 1.225
MTOW = 68731.*g #Maximum take-off weight in kg
S = 128. #wing surface area in m^2
A = 14.
e = 0.85
gamma_climb = radians(3) #degrees
hscr = 15.24 #screen height in m
C_L_maxto = (2.01)/(1.1**2) #CL max takeoff
C_Lcr = 0.87 #CL max cruise
C_Lland = 2.47  #CL max landing
C_L_cr = 0.6167
C_D_0 = 0.07 #CDO
thrust = 220000./2

W_a = 1431.5 #mass flow in lbs/sec
DF = 82 #fan diameter in inch
M_MO = 0.79 #Maximum operating mach number
lamda = 11. #bypass ratio
OPR = 40. #overall compression ratio
DIH = 0.037*W_a + 32.2 #Intake highlight diameter in inch
MH = 1.21*DF #Maximum height of main cowl in inch

LC = (2.36*DF)-(0.01*(DF*M_MO)**2) #Main cowl length in inch
DFO = ((0.00036*lamda*W_a)+5.84)**2 # Main cowl diameter at fan exit in inch
DMG = ((0.000475*lamda*W_a)+4.5)**2 # Gas generator cowl diameter at fan exit in inch
K = (log(1/(lamda+1))*(W_a/OPR))**2.2 
DJ = (18-(55*K))**0.5 #Gas generator cowl diameter at "hot" nozzle exit in inch
LAB = (DMG-DJ)*0.23 #length of gas generator afterbody in inch

print "--------Engine sizing by Jenkinson--------------"
print "The intake highlight diameter is", DIH*0.0254, "m"
print "The maximum height of the main cowl is", MH*0.0254, "m"
print "The Main cowl length is", LC*0.0254, "m"
print "The Main cowl diameter at fan exit is", DFO*0.0254, "m"
print "The gas generator cowl diameter at fan exit is", DMG*0.0254, "m"
print "The gas generator cowl diameter at hot nozzle exit is", DJ*0.0254, "m"
print "The length of the gas generator afterbody is", LAB*0.0254, "m"


