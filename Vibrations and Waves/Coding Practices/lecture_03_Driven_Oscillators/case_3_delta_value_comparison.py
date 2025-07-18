import os 
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
################################################################ 
############ Physical Parameters of Pendulum Bar ###############
################################################################
M   = 10    ## Mass of the pendulum bar
L   = 5     ## Length of the pendulum bar
MoI = (1/3)*M*np.square(L) ## Moment of Inertia of the pendulum bar 
B   = 5   ## Damping Costant
################################################################
##################### System Parameters ########################
################################################################
g             = 9.81  ## Gravitational acceleration
phi           = 0.0   ## phase delay
Theta_initial = np.deg2rad(0)
## Natural frequency of the pendulum bar
Omega_0       = np.sqrt(3*g/(2*L))  
## Damping constant 
Gamma         = 3*B/(M*np.square(L))  # Damping Coefficient
## Net frequency 
Omega         = np.sqrt(np.square(Omega_0) - (np.square(Gamma)/4))  
## input parameters
d             = 50 ## torque amplitude 
f0            = d/MoI
f             = 0.05  ## frequency of the periodic driving force 
Omega_d       = np.linspace(0,(np.pi),1000) ## 2*np.pi*f ## driving frequency
################################################################
##################### Governing Equation #######################
################################################################ 
def Calculate_Delta(OD):
    delta      = np.arctan((Gamma*OD)/(np.square(Omega_0) - np.square(OD)))   
    return delta

DD = [] 
Phi_shift_DD = []
for i in range(len(Omega_d)):
    omega_temp = Omega_d[i] 
    delta_temp = Calculate_Delta(omega_temp)
    DD.append(delta_temp) 
    if delta_temp >= 0:
        Phi_shift_DD.append(delta_temp) 
    elif delta_temp < 0:
        Phi_shift_DD.append(np.deg2rad(180)+delta_temp)
############################################################
############################################################
plt.figure(figsize=(9,6)) 
plt.plot(Omega_d,np.rad2deg(DD),color="teal",linewidth=2.0,label="Actual Value") 
plt.plot(Omega_d,np.rad2deg(Phi_shift_DD),color="crimson",linewidth=2.0,label="Phase shift value") 
plt.xlabel("Driving Frequency ($\omega_d$/s)")
plt.ylabel("$\delta$ ($\omega_d$) (in degree)")
plt.grid()
plt.legend(loc="best") 
plt.axvline(x=Omega_0,color="grey",alpha=0.5) 
plt.axhline(y=0,color="navy",linestyle="--") 
plt.axhline(y=180,color="navy",linestyle="--") 
plt.savefig("Delta_Plot_02Pi.jpg",dpi=360)
plt.show() 

