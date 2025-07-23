import os 
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
#######################################################
####################################################### 
g  = 9.81  # 1.62 #24.79 #9.81 ## gravity 
L  = 1.2  ## length of pendulum 
M  = 1.5  ## Mass of the pendulum 
K  = 5    ## stiffness of the Pendulum
#######################################################
####################################################### 
Omega_1  = np.sqrt(g/L)
Omega_2  = np.sqrt((g/L)+(2*K/M)) 
print("The system's first Natural Frequency  :",round(Omega_1,3)) 
print("The system's second Natural Frequency :",round(Omega_2,3)) 
#######################################################
#######################################################
# # Simulation 01 
# phi_1, phi_2 = 0,0 ## Assumption as zero
# X_0          = np.pi/6
# alpha, beta  = X_0/2, -X_0/2 

# t            = np.linspace(0,15,600) 
# X1           = 0.5*X_0*((np.cos(Omega_1*t))-(np.cos(Omega_2*t))) 
# X2           = 0.5*X_0*((np.cos(Omega_1*t))+(np.cos(Omega_2*t))) 

# plt.figure(figsize=(12,5)) 
# plt.plot(t,np.rad2deg(X1),label="X1") 
# plt.plot(t,np.rad2deg(X2),label="X2") 
# plt.plot(t,np.rad2deg(X1+X2),label="X1+X2",linewidth=2.0,color="green")
# plt.grid() 
# plt.xlabel("Time (in seconds)") 
# plt.ylabel("Position (in degree)") 
# plt.title("Coupled Pendulum for the value of (g = 9.81,L=1.2,M=1.5,K=5)")
# plt.legend(loc="best")
# plt.savefig("Coupled_Pendulum_Simulation_01.jpg",dpi=360)
# plt.show() 
#######################################################
#######################################################
## Simulation 02 

def Simulation_02(w1,w2,X0,T):
    X1 = -X0*np.sin(0.5*(w1+w2)*T)*np.sin(0.5*(w1-w2)*T) 
    X2 = X0*np.cos(0.5*(w1+w2)*T)*np.cos(0.5*(w1-w2)*T) 
    T_carrier = 2*np.pi/np.abs(0.5*(w1+w2)) 
    T_beat    = 2*np.pi/np.abs(w1-w2) 
    return X1,X2,T_carrier,T_beat 

T        = np.linspace(0,45,2700)  
X_0      = np.pi/6 

Omega_1                = 0.95*Omega_2
X1,X2,T_Carrier,T_beat = Simulation_02(Omega_1,Omega_2,X_0,T) 
Envelope_Frequency_X1  = -X_0*np.sin(0.5*(Omega_1-Omega_2)*T) 
Envelope_Frequency_X2  =  X_0*np.cos(0.5*(Omega_1-Omega_2)*T) 

plt.figure(figsize=(12,10)) 
plt.subplot(2,1,1)
plt.plot(T,np.rad2deg(X1),label="X1")
plt.plot(T,np.rad2deg(Envelope_Frequency_X1),label="X1 Envelope",color="grey",alpha=0.9)  
plt.plot(T,-np.rad2deg(Envelope_Frequency_X1),color="grey",alpha=0.9) 
plt.grid()
plt.title("Beat Phenomena (at Moon, g = 1.69)")
plt.legend(loc="best")
plt.xlabel("Position (in degrees)") 
plt.subplot(2,1,2) 
plt.plot(T,np.rad2deg(X2),label="X2")
plt.plot(T,np.rad2deg(Envelope_Frequency_X2),label="X2 Envelope",color="grey",alpha=0.9) 
plt.plot(T,-np.rad2deg(Envelope_Frequency_X2),color="grey",alpha=0.9) 
plt.grid() 
plt.legend(loc="best") 
plt.xlabel("Time (seconds)") 
plt.xlabel("Position (in degrees)") 
# plt.savefig("Beat_phenomena_Moon.jpg",dpi=360)
plt.show() 
#######################################################
#######################################################




