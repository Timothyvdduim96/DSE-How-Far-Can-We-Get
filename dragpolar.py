from math import *
import numpy as np
import matplotlib.pyplot as plt
from TWWS import C_Lcr

designdatalst = 'dop.csv'
designdata = np.genfromtxt(designdatalst, dtype='string', delimiter=';')

C_D_0_1 = eval(designdata[19][1])
C_D_0_2 = eval(designdata[19][2])
C_D_0_3 = eval(designdata[19][3])
C_D_0_4 = eval(designdata[19][4])
C_D_0_5 = eval(designdata[19][5])
C_D_0_6 = eval(designdata[19][6])
e = 0.85
A_1 = eval(designdata[12][1])
A_2 = eval(designdata[12][2])
A_3 = eval(designdata[12][3])
A_4 = eval(designdata[12][4])
A_5 = eval(designdata[12][5])
A_6 = eval(designdata[12][6])
K1 = 1/(pi*A_1*e)
K2 = 1/(pi*A_2*e)
K3 = 1/(pi*A_3*e)
K4 = 1/(pi*A_4*e)
K5 = 1/(pi*A_5*e)
K6 = 1/(pi*A_6*e)

CLlst1 = np.arange(0,1.38,0.01)
CDlst1 = []

for i in range(len(CLlst1)):
    CDlst1.append(C_D_0_1 + K1*CLlst1[i]**2)

CLlst2 = np.arange(0,C_Lcr,0.1)
CDlst2 = []

for i in range(len(CLlst2)):
    CDlst2.append(C_D_0_2 + K2*CLlst2[i]**2)

CLlst3 = np.arange(0,1.29,0.01)
CDlst3 = []

for i in range(len(CLlst3)):
    CDlst3.append(C_D_0_3 + K3*CLlst3[i]**2)

CLlst4 = np.arange(0,C_Lcr,0.1)
CDlst4 = []

for i in range(len(CLlst4)):
    CDlst4.append(C_D_0_4 + K4*CLlst4[i]**2)

CLlst5 = np.arange(0,C_Lcr,0.1)
CDlst5 = []

for i in range(len(CLlst5)):
    CDlst5.append(C_D_0_5 + K5*CLlst5[i]**2)

CLlst6 = np.arange(0,C_Lcr,0.1)
CDlst6 = []

for i in range(len(CLlst6)):
    CDlst6.append(C_D_0_6 + K6*CLlst6[i]**2)

plt.xlabel("C_D")
plt.ylabel("C_L")
plt.plot(CDlst1,CLlst1,label='Design 1 & 2')
#plt.plot(CLlst2,CDlst2)
plt.plot(CDlst3,CLlst3,label='Design 3, 4, 5 & 6')
#plt.plot(CLlst4,CDlst4)
#plt.plot(CLlst5,CDlst5)
#plt.plot(CLlst6,CDlst6)
ax = plt.subplot(111)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()
plt.show()
