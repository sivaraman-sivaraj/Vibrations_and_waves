import os 
import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
############################################
############################################
M = 5 
K = 8 
wa = np.sqrt(K/M) 
wb = np.sqrt((2*K)/M) 

T = np.linspace(0,60,1200) 
A,B = -0.2, 0.0

X1 = B*np.cos((wb*T))
X2 = (A*np.cos((wa*T))) - (B*np.cos((wb*T))) 
X3 = (-A*np.cos((wa*T))) - (B*np.cos((wb*T))) 

plt.figure(figsize=(12,9)) 
plt.subplot(3,1,1) 
plt.plot(T,X1) 
plt.grid()
plt.subplot(3,1,2)
plt.plot(T,X2) 
plt.grid() 
plt.subplot(3,1,3)
plt.plot(T,X3)
plt.grid()
plt.show() 

