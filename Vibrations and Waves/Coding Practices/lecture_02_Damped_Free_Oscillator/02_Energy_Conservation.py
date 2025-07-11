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
Xd  = -X_initial*omega_0**np.sin((omega_0*t)+phi) 


Potential_Energy = 0.5*K*(np.square(X)) 
Kinetic_Energy   = 0.5*M*np.square(np.gradient(X)*100)
# Kinetic_Energy   = 0.5*M*(np.square(Xd))
Total_Energy = Potential_Energy + Kinetic_Energy

# plt.plot(Kinetic_Energy) 
# plt.show() 


plt.figure(figsize=(9,6)) 
plt.plot(t,Kinetic_Energy,color="red",linewidth=2.0,label="Kinetic Energy") 
plt.plot(t,Potential_Energy,color="g",label="Potential Energy",linewidth=2.0) 
plt.plot(t,Total_Energy,color="b",label="Total Energy",linewidth=2.5) 
plt.grid(True)
plt.xlabel("Time (in seconds)") 
plt.ylabel("Energy (in joules)") 
plt.axhline(y=0,color="grey",alpha=0.2) 
plt.axvline(x=0,color="grey",alpha=0.2) 
plt.legend(loc="best") 
plt.title("Energy Conservation") 
plt.savefig("Conserved_Energy.jpg",dpi=420)
plt.show() 
#########################################################
#########################################################