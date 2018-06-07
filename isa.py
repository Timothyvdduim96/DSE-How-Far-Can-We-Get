from math import e

R = 287.05
g = 9.80665

lapselst = [-.0065,0,.001,.0028,0,-.0028,-.002,0.]
hlst = [0,11000,20000,32000,47000,51000,71000,84852,100000]
T0lst = [288.15]
p0lst = [101325]

for i in range(1,8):
    T0 = T0lst[i-1] + lapselst[i-1]*(hlst[i]-hlst[i-1])
    T0lst.append(T0)
    
    if lapselst[i-1] != 0:
        p0 = p0lst[i-1] * (T0lst[i]/T0lst[i-1])**(-g/(lapselst[i-1]*R))
    else:
        p0 = p0lst[i-1] * e**(-g/(R*T0lst[i])*(hlst[i]-hlst[i-1]))

    p0lst.append(p0)

#print p0lst
#print T0lst

def ISA(h):
    for i in range(8):
        if hlst[i] < h <= hlst[i+1]:
            h0 = hlst[i]
            T0 = T0lst[i]
            p0 = p0lst[i]
            a  = lapselst[i]
            
            if a != 0:
                T = T0 + a*(h-h0)
                p = p0 * (T/T0)**(-g/(a*R))
            else:
                T = T0
                p = p0 * e**(-g/(R*T0)*(h - h0))

            rho = p / (R*T)

    return T,p,rho

def ISA_rho(rho):
    T0 = T0lst[0]
    a  = lapselst[0]
    if rho > ISA(11000)[2]:
        h = ((rho/1.225)**((-g/(a*R)-1)**-1)-1)*T0/a
    return h

print ISA_rho(1.225)