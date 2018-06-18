from math import *
import matplotlib.pyplot as plt
from parameters import *
from systemsprepaircraft import frontcg,aftcg,x_lemac_lst
#---------------------------------PARAMETERS---------------------------------------

shift = np.arange(0,0.025,0.005)
xlemaclst1 = []
xlemaclst2 = []
xlemaclst3 = []
xlemaclst4 = []

for i in range(len(shift)):
    for j in range(len(frontcg)):
        if i == 0:
            z = x_lemac_lst[j]+shift[i]
            xlemaclst1.append(z)
        if i == 1:
            xlemaclst2.append(x_lemac_lst[j]+shift[i])
        if i == 2:
            xlemaclst3.append(x_lemac_lst[j]+shift[i])
        if i == 3:
            xlemaclst4.append(x_lemac_lst[j]+shift[i])

SM = 0.05
M = value("M_cr")
A_h = value("Ah")
A = value("A")
c_r = value("c_r")
c_t = value("c_t")
MAC = value("MAC")
d_ext_fus = 4 #value("d_ext_fus")
taper_h = value("ct_h")/value("cr_h")
beta = sqrt(1-M**2)
eta = 0.95
taper = value("taper")
sweep_05_Ch = atan(tan(np.radians(value("sweep_h"))) - (4/A_h)*(0.5*(1-taper_h)/(1+taper_h)))
C_L_alpha_h = 2*pi*A_h/(2 + sqrt(4 + (A_h*beta/eta)**2*(1 + tan(sweep_05_Ch)**2/beta**2)))
S = value("S")
C_L_alpha_w = value("CL_alpha_cruise_clean")
b_f = 4 #value("d_ext_fus")
b = value("b")
l_f = value("l_fus")
S_net = S - d_ext_fus*value("c_r")
C_L_alpha_Ah = C_L_alpha_w*(1 + 2.15*b_f/b)*S_net/S + pi/2*b_f**2/S
r = value("l_h")/(b/2)
m_tv = 0.3                                                          #ROUGH APPROX., CHECK WITH HARRY LATER
lambda_14_w = value("lambdac_4")
def downwash():
    K_eps_lambda = (0.1124 + 0.1265*lambda_14_w + 0.1766*lambda_14_w**2)/r**2 + 0.1024/r + 2
    K_eps_lambda0 = 0.1124/r**2 + 0.1024/r + 2
    downwash = K_eps_lambda/K_eps_lambda0*(r*0.4876/((r**2 + m_tv**2)*sqrt(r**2 + 0.6319 + m_tv**2)) + (1 + (r**2/(r**2 + 0.7915 + 5.0734*m_tv**2))**0.3113)*(1 - sqrt(m_tv**2/(1 + m_tv**2))))*C_L_alpha_w/(pi*A)

    return downwash
downwash = downwash()
l_h = value("l_h")
c_bar = value("MAC")
V_h_over_V = sqrt(0.85)
C_L_h = -0.8
C_L_Ah = 2.2 #CHANGE, LINK TO PAR FILE
h_f = 4 #value("d_ext_fus")
c_g = S/b
l_fn = value("x_lemac") - cos(np.degrees(value("lambdac_0")))*((c_r - MAC)/((c_r-c_t)/((b-d_ext_fus/2)/2)))
x_bar_ac_wf = 0.35 - 1.8/C_L_alpha_Ah*b_f*h_f*l_fn/(S*c_bar) + 0.273/(1 + taper)*b_f*c_g*(b - b_f)/(c_bar**2*(b + 2.15*b_f))*tan(lambda_14_w)
l_n = 3.25  #value("l_n")
b_n = 2.334 #CHECK/LINK LATER
k_n = 4.0
x_bar_ac_n = k_n*b_n**2*l_n/(S*c_bar*C_L_alpha_Ah)/2
x_bar_ac = x_bar_ac_wf + x_bar_ac_n
C_L_0 = 0.31
C_m_0_airfoil = -0.114
C_m_ac_w = C_m_0_airfoil*(A*cos(value("lambdac_0"))**2/(A + 2*cos(value("lambdac_0"))))
mu_1 = 0.2
mu_2 = 0.65
mu_3 = 0.057
delta_C_l_max = value("dCL_HLD_land")
c_ratio = value("c_ext_c_land")
S_wf = S + value("S_flaps_land")
C_m_ac_flaps = mu_2*(-mu_1*delta_C_l_max*c_ratio - (C_L_Ah + delta_C_l_max*(1 - S_wf/S))/8*c_ratio*(c_ratio - 1)) + 0.7*A/(1 + 2/A)*mu_3*delta_C_l_max*tan(lambda_14_w) - C_L_Ah*(0.25 - x_bar_ac)
C_m_ac_fus = -1.8*(1 - 2.5*b_f/l_f)*pi*b_f*h_f*l_f/(4*S*c_bar)*C_L_0/C_L_alpha_Ah/value("CL_alpha_low_clean")*C_L_alpha_w
C_m_ac_nac = -0.05
C_m_ac = C_m_ac_w + C_m_ac_flaps + C_m_ac_fus + C_m_ac_nac

x_bar_cg = np.arange(-0.2,1+0.001,0.001)
Sh_S_stab = []
Sh_S_stab_2 = []
Sh_S_cont = []

#---------------------------------STABILITY----------------------------------------
for i in x_bar_cg:
    
    m = (C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)**-1
    q = -(x_bar_ac - SM)/(C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)

    Sh_S_stab.append(m*i + q)

for i in x_bar_cg:
    
    m = (C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)**-1
    q = -(x_bar_ac)/(C_L_alpha_h/C_L_alpha_Ah*(1-downwash)*l_h/c_bar*(V_h_over_V)**2)

    Sh_S_stab_2.append(m*i + q)

#---------------------------------CONTROLLABILITY--------------------------------------

for i in x_bar_cg:
    n = (C_L_h/C_L_Ah*l_h/c_bar*(V_h_over_V)**2)**-1
    p = (C_m_ac/C_L_Ah-x_bar_ac)/(C_L_h/C_L_Ah*l_h/c_bar*(V_h_over_V)**2)

    Sh_S_cont.append(n*i + p)


##fig, ax1 = plt.subplots()
##ax1.plot(frontcg,xlemaclst1, color="black")
##ax1.plot(aftcg,xlemaclst1, color="black")
###ax1.plot(frontcg,xlemaclst2, color="green")
###ax1.plot(aftcg,xlemaclst2, color="green")
###ax1.plot(frontcg,xlemaclst3, color="brown")
###ax1.plot(aftcg,xlemaclst3, color="brown")
###ax1.plot(frontcg,xlemaclst4, color="cyan")
###ax1.plot(aftcg,xlemaclst4, color="cyan")
##ax1.axis((-1,1.5,xlemaclst3[0],xlemaclst3[len(xlemaclst1)-1]))
##ax1.set_xlabel('x_cg/MAC')
### Make the y-axis label, ticks and tick labels match the line color.
##ax1.set_ylabel('X_lemac/l_fus', color='b')
##ax1.tick_params('y', colors='b')
##
##ax2 = ax1.twinx()
##ax2.plot(x_bar_cg,Sh_S_cont,label="Controllability")
##ax2.plot(x_bar_cg,Sh_S_stab,label="Stability incl. S.M.")
##ax2.axis((-1,1.5,0,max(max(Sh_S_stab),max(Sh_S_cont))))
##ax2.set_ylabel('S_h/S', color='r')
##ax2.tick_params('y', colors='r')
##
##fig.tight_layout()
##plt.show()

plt.plot(x_bar_cg,Sh_S_cont,label="Controllability")
#plt.plot(x_bar_cg,Sh_S_stab_2,label="Neutral stability")
plt.plot(x_bar_cg,Sh_S_stab,label="Stability incl. S.M.")
plt.axis((0,max(x_bar_cg),0,max(max(Sh_S_stab),max(Sh_S_cont))))
##ax = plt.subplot(111)
##box = ax.get_position()
##ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
##ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel("x_bar_cg")
plt.ylabel("Sh/S")
plt.grid()
plt.show()
