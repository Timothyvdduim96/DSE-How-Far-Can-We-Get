from math import *
import numpy as np
import sympy
from scipy.integrate import quad

#------------------------------------------------upper coordinates-----------------------------------------------------------

uppercoord = 'uppersurface.txt'

uppercoord = np.genfromtxt(uppercoord, dtype='string', delimiter=';')

uppercoordin = []

for i in range(len(uppercoord)):
    uppercoordin.append(uppercoord[i].split())

xcoordupper = []
ycoordupper = []

for i in range(len(uppercoordin)):
    xcoordupper.append(eval(uppercoordin[i][0]))
    ycoordupper.append(eval(uppercoordin[i][1]))

uppoly = np.polyfit(xcoordupper,ycoordupper,5)

x = np.arange(0,1,0.001)
yupper = []

def fupper(x):

    return uppoly[0]*x**(len(uppoly)-1) + uppoly[1]*x**(len(uppoly)-2) + uppoly[2]*x**(len(uppoly)-3) + uppoly[3]*x**(len(uppoly)-4) + uppoly[4]*x**(len(uppoly)-5) + uppoly[5]*x**(len(uppoly)-6)

print "poly upper part = ", uppoly[0], "x^", len(uppoly)-1, "+", uppoly[1], "x^", len(uppoly)-2, "+", uppoly[2], "x^", len(uppoly)-3, "+", uppoly[3], "x^", len(uppoly)-4, "+", uppoly[4], "x^", len(uppoly)-5, "+", uppoly[5]
for i in range(len(x)):
    yupper.append(fupper(x[i]))

#-----------------------------------------------lower coordinates------------------------------------------------------------

lowercoord = 'lowersurface.txt'

lowercoord = np.genfromtxt(lowercoord, dtype='string', delimiter=';')

lowercoordin = []

for i in range(len(lowercoord)):
    lowercoordin.append(lowercoord[i].split())

xcoordlower = []
ycoordlower = []

for i in range(len(lowercoordin)):
    xcoordlower.append(eval(lowercoordin[i][0]))
    ycoordlower.append(eval(lowercoordin[i][1]))

lowpoly = np.polyfit(xcoordlower,ycoordlower,5)

ylower = []

def flower(x):

    return lowpoly[0]*x**(len(lowpoly)-1) + lowpoly[1]*x**(len(lowpoly)-2) + lowpoly[2]*x**(len(lowpoly)-3) + lowpoly[3]*x**(len(lowpoly)-4) + lowpoly[4]*x**(len(lowpoly)-5)

print "poly lower part = ", lowpoly[0], "x^", len(lowpoly)-1, "+", lowpoly[1], "x^", len(lowpoly)-2, "+", lowpoly[2], "x^", len(lowpoly)-3, "+", lowpoly[3], "x^", len(lowpoly)-4, "+", lowpoly[4], "x^", len(lowpoly)-5, "+", lowpoly[5]

for i in range(len(x)):
    ylower.append(flower(x[i]))
    
#--------------------------------------------difference coordinate--------------------------------------------------------------

def fdiff(x):

    diff = fupper(x)-flower(x)

    return diff

xr = np.arange(0,1,0.01)
imp = []
for i in range(len(xr)):
    imp.append(fdiff(xr[i]))
