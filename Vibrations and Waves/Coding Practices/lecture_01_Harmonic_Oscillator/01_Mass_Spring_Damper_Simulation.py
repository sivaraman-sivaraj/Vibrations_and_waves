import os 
import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt
################################################
K         = 10  ## define the stifness here
M         = 15  ## define the mass of the system here
X_initial = 1.5 ## initial condition

### The natural frequency of the system 
omega_0 = np.sqrt(K/M) 
print("The system's natural frequency of the system is :", str(round(omega_0,4)))
###################################################################
################################################################### 
#### Properties
t   = np.linspace(0,10,1000) ## define the time here
phi = np.deg2rad(0)          ## phase lag, change here to observe the nature 
X   = X_initial*np.cos((omega_0*t)+phi) 
## Simulation in Time Domain
## for understanding the phase delay
X_p30   = X_initial*np.cos((omega_0*t)+np.deg2rad(30)) 
X_p45   = X_initial*np.cos((omega_0*t)+np.deg2rad(45))
X_p60   = X_initial*np.cos((omega_0*t)+np.deg2rad(60))
X_p30m   = X_initial*np.cos((omega_0*t)+np.deg2rad(-30)) 
X_p45m   = X_initial*np.cos((omega_0*t)+np.deg2rad(-45))
X_p60m   = X_initial*np.cos((omega_0*t)+np.deg2rad(-60))
###
plt.figure(figsize=(12,5)) 
plt.plot(t,X,color="crimson",linewidth=2,label="phi = 0") 
plt.plot(t,X_p30,color="blue",alpha=0.2,label="phi = 30$\degree$",linestyle="--")
plt.plot(t,X_p45,color="navy",alpha=0.2,label="phi = 45$\degree$",linestyle="--")
plt.plot(t,X_p30m,color="lime",alpha=0.2,label="phi = -30$\degree$",linestyle="--")
plt.plot(t,X_p45m,color="seagreen",alpha=0.2,label="phi = -45$\degree$",linestyle="--")
plt.xlabel("Time (in seconds)") 
plt.ylabel("Amplitude (in meters)") 
plt.grid() 
plt.legend(loc="best") 
plt.axhline(y=0,color="black",linewidth=2.0)
plt.axvline(x=0,color="black",linewidth=2.0) 
plt.title("Lecture 01 : Harmonic Oscillation ")
plt.savefig("TD_simulation.jpg",dpi=420) 
plt.show() 
####################################################################
####################################################################
### In complex plane representation 
RP = X_initial*np.cos((omega_0*t)+phi) 
IP = X_initial*np.sin((omega_0*t)+phi) 
IP_sine_square = X_initial*np.square(np.sin((omega_0*t)+phi)) 
IP_sin_cos     = X_initial*np.sin((omega_0*t)+phi)*np.cos((omega_0*t)+phi)

plt.figure(figsize=(8,8)) 
plt.plot(RP,IP,color = "orchid",linewidth=2.0,label="IP = sin(theta)") 
plt.plot(RP,IP_sine_square,color = "navy",linewidth=2.0,label="IP = sin^2(theta)") 
plt.plot(RP,IP_sin_cos,color="tan",linewidth=2.0,label="IP = sin(t)*cos(t)")
plt.grid()
plt.xlabel("Real part")
plt.ylabel("Imaginary Part") 
plt.title("Complex representation (for different imaginary parts)") 
plt.axhline(y=0,color="black",linewidth=2.0)
plt.axvline(x=0,color="black",linewidth=2.0)  
plt.legend(loc="best")
plt.savefig("02_MSD_Complex_Representation.jpg",dpi=420) 
plt.show() 



