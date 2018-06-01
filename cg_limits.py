# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:14:16 2018

@author: mrvan
"""



from scipy.integrate import quad
from scipy import optimize as opt
import numpy as np
import matplotlib.pyplot as plt
from math import *

MAC =
L_fus = 
L_cabin =
L_nose =

Wemp =    # fraction of MTOW
Wfus =
Wnac =
Wprop =
Wfix =
Wwing =

Xemp =     # [m] 
Xfus =
Xnac =
Xprop =
Xfix =
Xwing = 



XcgOEW = 0.25 # [MAC]
Xfcg = (Wemp*Xemp+Wfus*Xfus+Wfix*Xfix)/(Wemp+Wfus+Wfix) # [m]  (measured from nose)
Mw = Wwing + Wprop + Wnac
Mf = Wfus + Wemp + Wfix
Xwcg = 0.4    # [MAC]

Xlemac = Xfcg + MAC*(Xwcg*(Mw/Mf)-XcgOEW*(1+Mw/Mf))

OEW = 
Wpl =
Wf = 

Xcgpl =  L_nose+L_cabin/2.  #[m]
Xcgf =    #[m]


XcgOEWm = (Wemp*Xemp+Wfus*Xfus+Wnac*Xnac+Wprop*Xprop+Wfix*Xfix+Wwing*Xwing)/(Wemp+Wfus+Wnac+Wprop+Wfix+Wwing)
XcgOEW_pl =  (Wemp*Xemp+Wfus*Xfus+Wnac*Xnac+Wprop*Xprop+Wfix*Xfix+Wwing*Xwing + Wpl*Xcgpl)/(Wemp+Wfus+Wnac+Wprop+Wfix+Wwing+Wpl)
XcgOEW_f =  (Wemp*Xemp+Wfus*Xfus+Wnac*Xnac+Wprop*Xprop+Wfix*Xfix+Wwing*Xwing + Wf*Xcgf)/(Wemp+Wfus+Wnac+Wprop+Wfix+Wwing+Wf)
XcgOEW_pl_f =  (Wemp*Xemp+Wfus*Xfus+Wnac*Xnac+Wprop*Xprop+Wfix*Xfix+Wwing*Xwing + Wpl*Xcgpl+Wf*Xcgf)/(Wemp+Wfus+Wnac+Wprop+Wfix+Wwing+Wpl+Wf)
