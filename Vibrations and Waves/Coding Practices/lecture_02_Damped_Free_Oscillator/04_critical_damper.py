import os 
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
############################################ 
### Parameters of Pendulum Bar
M   = 10    ## Mass of the pendulum bar
L   = 5     ## Length of the pendulum bar
MoI = (1/3)*M*np.square(L) ## Moment of Inertia of the pendulum bar 
B   = 36     ## Damping Coefficient
############################################ 
g   = 9.81  ## Gravitational acceleration
phi = 0.0   ## phase delay
Theta_initial = np.deg2rad(30)
Omega_0 = np.sqrt(3*g/(2*L)) 
##############################################
def critical_B(Omw_0):
    Gamma_c = np.sqrt(4*np.square(Omw_0)) 
    return Gamma_c 

def require_damping(Gamma1,M1,L1):
    C0 = Gamma1*M*(L**2)/3 
    print("The Required critical damping value is :",C0) 
    return  C0

Gamma = critical_B(Omega_0) 
C0    = require_damping(Gamma,M,L)
##############################################
def Critical_Damped(Gamma,Theta_initial):
    A     = Theta_initial 
    B     = 0.0
    ### simulation 
    t = np.linspace(0, 10, 1000)
    Theta_t = (Theta_initial+(B*t))*np.exp(-0.5*Gamma*t) 
    plt.figure(figsize=(12,5)) 
    plt.plot(t,np.rad2deg(Theta_t),color="teal",linewidth=2.0) 
    plt.grid(True) 
    plt.xlabel("Time (in seconds)") 
    plt.ylabel("Theta (in degree)") 
    plt.title("System with critically damped conidtion")
    plt.axhline(y=0,color="grey",linewidth=2.0) 
    plt.axvline(x=0,color="grey",linewidth=2.0) 
    plt.savefig("Pendulum_bar_critical_damped_2d.jpg",dpi=420)
    plt.show() 
    return t,np.rad2deg(Theta_t)


_,_ = Critical_Damped(Gamma,Theta_initial)