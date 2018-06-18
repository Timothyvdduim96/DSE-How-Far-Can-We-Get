#################Wing Design Tool########################
from parameters import *
from Fuselage_Structure import *
from material_database import *

def Uni_load(w,L,E,I,x):
    d=(w*x**2)/(24*E*I)*(x**2-4*L*x+6*L**2);
    return d 

def Point_load(P,E,I,a,x):
    if x<a:
        d=P*x**3/(3*E*I);
    else:
        d=P*a**3/(3*E*I)+(P*a**2)/(2*E*I)*(x-a);
    return d
    
def Axial(P,L,E,A):
    d=P*L/(E*A);
    return d

def Pytha(x,y):
    d=sqrt(x**2+y**2);
    return d

def Thin_walled_circle(R,t):
    Area=2*pi*R*t;
    I=pi*R**3*t;
    return Area,I

def Buckling(E,I,K,L): 
    Pcr=(pi**2*E*I)/(K*L)**2;
    return Pcr

def Axial_Stress(F,A):
    stress=F/A;
    return stress
    
def Inertia_Wing(b,h,t1,t2):
    Area=b*h-(b-2*t1)*(h-2*t2);
    Inertia=(1/12.)*(b*h**3)-(1/12.)*(b-2*t1)*(h-2*t2)**3;
    return Area,Inertia
    
#Dimensions
L_wing=b/2
y_eng=0.321*L_wing

#Forces
F_eng=W_eng*g*n/2
F_fuel=(W_fuel_wing)*g*n/2
F_wing=W_wing*g*n/2
F_MTOW=MTOW*g*n/2    
F_rest=F_MTOW-F_fuel-F_wing
w=(F_rest)/L_wing    

#Strut Dimensions + Materials
h_strut=3.5
theta_strut=atan(h_strut/y_eng)
L_strut=Pytha(y_eng,h_strut)
E_strut=E_Alu_2*10**9
[A_strut,I_strut]=Thin_walled_circle(100*mm_to_m,10*mm_to_m)

#Wingbox + Material
x_spar_1=0.20*MAC
x_spar_2=0.65*MAC
h_spar=0.10*MAC
b_spar=x_spar_2-x_spar_1
E_wing=E_CFRP*10**9
[A_wing,I_wing]=Inertia_Wing(MAC,h_spar,30*mm_to_m,30*mm_to_m)    

Elis=np.linspace(E_CFRP*10**9/10.,E_CFRP*10**9*10,100)
lis=[]
####Solve for Strut Reaction Force#####
for i in Elis:
    E_wing=i
    v_lift=Uni_load(w,L_wing,E_wing,I_wing,y_eng)
    v_eng=Point_load(F_eng,E_wing,I_wing,y_eng,y_eng)
    num=v_lift-v_eng
    a=L_strut/(E_strut*A_strut)
    b=y_eng**2/(3*E_wing*I_wing)
    den=sin(theta_strut)*(a+b)
    F_strut=num/den
    ratio=F_strut/F_rest
    lis.append(ratio)
plt.plot(Elis,lis)    