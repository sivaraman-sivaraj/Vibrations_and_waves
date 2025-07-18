import os 
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
################################################################ 
############ Physical Parameters of Pendulum Bar ###############
################################################################
M   = 8.1    ## Mass of the pendulum bar
L   = 8     ## Length of the pendulum bar
MoI = (1/3)*M*np.square(L) ## Moment of Inertia of the pendulum bar 
B   = 10   ## Damping Costant
################################################################
##################### System Parameters ########################
################################################################
g             = 9.81  ## Gravitational acceleration
phi           = 0.0   ## phase delay
Theta_initial = np.deg2rad(-60)
## Natural frequency of the pendulum bar
Omega_0       = np.sqrt(3*g/(2*L))  
## Damping constant 
Gamma         = 3*B/(M*np.square(L))  # Damping Coefficient
## Net frequency 
Omega         = np.sqrt(np.square(Omega_0) - (np.square(Gamma)/4))  
## input parameters
d             = 50 ## torque amplitude 
f0            = d/MoI
f             = 0.1  ## frequency of the periodic driving force 
Omega_d       = 2*np.pi*f ## driving frequency
################################################################
##################### Governing Equation #######################
################################################################ 
A_wd       = f0/np.sqrt(np.square(np.square(Omega_0) - np.square(Omega_d))+(np.square(Omega_d)*np.square(Gamma))) 
delta      = np.arctan((Gamma*Omega_d)/(np.square(Omega_0) - np.square(Omega_d)))   

B          = Theta_initial/np.cos(phi)

## Time 
t         = np.linspace(0,160,2600)
#### Driving Torque 
T_drive   = f0*np.cos((Omega_d*t)) 
Theta_act = (A_wd*np.cos((Omega_d*t)-delta)) + (B*np.exp(-0.5*Gamma*t)*np.cos((Omega*t)+phi))


############################################################
############################################################
plt.figure(figsize=(12,5)) 
plt.plot(t,np.rad2deg(T_drive),color="crimson",linestyle="--",linewidth=2.0,label="Driven Force") 
# plt.plot(t,np.rad2deg(np.cos((Omega_d*t))))
plt.plot(t,np.rad2deg(Theta_act),color="teal",linewidth=2.0,label="Pendulum Bar")
plt.grid()
plt.xlabel("Time (in seconds)") 
plt.ylabel("Amplitude (in degree)") 
plt.legend(loc="best") 
plt.savefig("Sim_01_Driving_Force.jpg",dpi=360)
plt.show() 
#############################################
############ How it is damped ? #############
############################################# 
def How_is_is_damped(wo,Gamma):
    type_id = 0
    if np.square(wo) > (np.square(Gamma)/4):
        print("The system is underdamped...!")
        type_id = 1
    elif np.square(wo) == (np.square(Gamma)/4) :
        print("The System is critically damped...!")
        type_id = 2
    elif np.square(wo) < (np.square(Gamma)/4):
        print("The system is overdamped...!")
        type_id = 3
    else:
        print("please check the system's parameters.")
    return type_id
############################################################