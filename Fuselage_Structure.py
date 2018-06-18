########################Fuselage Structural Analysis Tool#######################
from parameters import *

density_fuel=810

n=2.5*1.25
b=value("b")
S=value("S")
l_fus=value("l_fus")
V_LOF=value("V_LOF")
T=value("thrust")
T=T*10**3
r=value("r_ext_fus")

#Component Weights
MTOW=value("MTOW")
W_wing=value("W_wing")
W_prop=value("W_propulsion")
W_nac=value("W_nacelle")
W_fuel=value("W_fuel")
W_eng=W_prop+W_nac
MAC=value("MAC")
MAC_h=value("MAC_h")
W_landing=61469

#Fuel Weights
W_fuel_wing=(14500)*density_fuel*10**-3
W_fuel_wing_landing=3900 #kg
W_fuel_centertank=0*density_fuel*10**-3
W_fuel_tail=513*density_fuel*10**-3
R_fus=2.0

#Wing Positions
h_wing=r
x_lemac=18.38
x_cg_wing=x_lemac+0.5*MAC
margin_tail=1
x_cg_tail=l_fus-0.5*MAC_h-margin_tail
l_h=x_cg_tail-x_cg_wing

#####Calculation of Wing and Tail Lift Take-off################

####Take-off#####
theta_TO=4.5*deg_to_rad
alpha_TO=0.5*deg_to_rad

C_m_w=-0.12
V_TO=85.34
M_w=C_m_w*q(V_TO,0)*S*MAC

####Engine Parameters#####
d_eng=1.993
r_eng=d_eng/2
h_eng_fairing=0.13
z_eng_wing=r_eng+h_eng_fairing-h_wing
M_T=z_eng_wing*T

def Centroid(m,x):
    num=0
    for i in range(len(m)):
        num=num+m[i]*x[i]
    xcg=num/sum(m)
    return xcg


###Weight Distribution####
W_A=W_wing+W_eng+W_fuel_wing+W_fuel_centertank
W_B=W_fuel_tail
W_rest=MTOW-W_A-W_B
W_array=[MTOW,W_A,W_B]
x_array=[l_fus/2,x_cg_wing,x_cg_tail]
x_cg=Centroid(W_array,x_array)
x_ct=19    
def Lift_wings(M_w,T,z_EW,n,W,x_cg,x_w,l_h,alpha,theta):
    L_t=(M_w+T*z_EW+n*W*cos(theta)*g*(x_cg-x_w))/(l_h*cos(alpha))
    L_w=(n*W*cos(theta))/(cos(alpha))-L_t
    
    return L_w,L_t

[L_wing,L_tail]=Lift_wings(M_w,T,z_eng_wing,n,MTOW,x_cg,x_cg_wing,l_h,alpha_TO,theta_TO)
w_rest=W_rest/l_fus


def Fuselage_Shear_z(x):
    if 0<x<x_cg_wing:
        V=-w_rest*g*n*x
        
    elif x_cg_wing<x<x_cg_tail:
        V=-w_rest*g*n*x+(L_wing-W_A*g*n)
        
    else :
        V=-w_rest*x+(L_wing-W_A*g*n)+(L_tail-W_B*g*n)
    return V

def Fuselage_Moment_z(x):
    if 0<x<x_cg_wing:
        M=-w_rest*g*n*x*2/2.
        
    elif x_cg_wing<x<x_cg_tail:
        M=-w_rest*g*n*x*2/2+(L_wing-W_A*g*n)*(x-x_cg_wing)+M_w+M_T
    else :
        M=-w_rest*g*n*x*2/2+(L_wing-W_A*g*n)*(x-x_cg_wing)+M_w+M_T+(L_tail-W_B*g*n)*(x-x_cg_tail)
    return M

x=np.linspace(0,l_fus,1000)
Vlist=[]
Mlist=[]
for i in x:
    V=Fuselage_Shear_z(i)
    Vlist.append(V)
    M=Fuselage_Moment_z(i)
    Mlist.append(M)    
plt.plot(x,Mlist)


plt.grid()

#################Landing#################
W_landing=61469
V_M=W_landing*(n-1)/2
z_lg=1.5
T_fus=1.4*V_M*(z_lg+r)
String_Fuselage_Structure=["a"]
