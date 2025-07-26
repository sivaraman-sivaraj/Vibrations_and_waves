import os 
import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
################################################
################################################
K = 5
M = 3
L = 1.5 
g = 9.81 
## Initial Condition 
X10,X20      = np.pi/6, 0 
phi1, phi2   = 0.0, 0.0
## Natural Frequency 
w1 = np.sqrt(g/L) 
w2 = np.sqrt((g/L)+(2*K/M)) 
## Driving Frequency & Driving Force
wd = 2*np.pi*0.005 
F0 = 1
## State Space Equation 
A11 = (K/M)+(g/L)- np.square(wd) 
A12 = -K/M 
A21 = -K/M 
A22 = (K/M)+(g/L)- np.square(wd) 
## state space matrix
E = np.array([[A11,A12],[A21,A22]]) 
## coupling matrix 
D11 = F0/M
D21 = 0 

D  = np.array([[D11],[D21]])
## Governing Equation  E.B = D
################################################
################################################ 
print("The natural frequency of the system : $\omega_1$ & $\omega_2$ :", str(round(w1,3)),str(round(w2,3))) 
print("The driven frequency of the system :", str(round(wd,3))) 
################################################
################################################  
## Applying cramer's rule to find B value 

## B11 
B1M = np.array([[D11,A12],[D21,A22]]) 
B2M = np.array([[A11,D11],[A21,D21]]) 

B11 = np.linalg.det(B1M)/np.linalg.det(E) 
B21 = np.linalg.det(B2M)/np.linalg.det(E) 
print("The driven frequeny co-efficients are :",str(round(B11,3)),str(round(B21,3)))
## Co-efficients Calculation
alpha = (X10 + X20 - B11 - B21)*0.5
beta  = (X10 - X20 - B11 + B21)*0.5
### Assertio on the calculated co-efficients 
X1assert = alpha + beta + B11
print("The coefficients Accuracy",str(round(X10,3)),str(round(X1assert,3)),"--> these value should be close to each other")
################################################
################################################ 
## Simulation 
t = np.linspace(0,30,600) 

X1P = (alpha*np.cos((w1*t)+phi1)) + (beta*np.cos((w2*t)+phi2)) + (B11*np.cos(wd*t)) 
X2P = (alpha*np.cos((w1*t)+phi1)) - (beta*np.cos((w2*t)+phi2)) + (B21*np.cos(wd*t)) 
################################################
################################################
# plt.figure(figsize=(9,6)) 
# plt.subplot(2,1,1)
# plt.plot(t,np.rad2deg(X1P),label="$X_1$")
# plt.ylabel("Position (in degrees)") 
# plt.title("Driven Simulation of Coupled Pendulum") 
# plt.grid()
# plt.legend(loc="best") 
# # plt.tight_layout()
# plt.subplot(2,1,2)
# plt.plot(t,np.rad2deg(X2P),label="$X_2$") 
# plt.xlabel("Time (s)")
# plt.grid() 
# plt.legend(loc="best") 
# plt.ylabel("Position (in degrees)") 
# plt.savefig("Normal_Simulation.jpg",dpi=360)
# plt.show()
################################################
def Create_GIF(T,X,X2):
    fig,ax = plt.subplots(figsize=(12,5)) 
    ax.set_xlim(T[0] - 0.2, T[-1] + 0.2)
    ax.set_ylim(-32, 32) ## <-- pay attention here..!
    ax.set_title("The System's amplitude in time domain")
    ax.set_xlabel("Time (in Seconds)")
    ax.set_ylabel("Amplitude (in degree)")
    ax.grid()
    ########################
    X1_traj, = ax.plot([], [], 'coral', lw=1.2, label='X1')
    X1_dot,  = ax.plot([], [], 'ro',markersize=6) 
    X2_traj, = ax.plot([], [], 'navy', lw=1.2, label='X2')
    X2_dot,  = ax.plot([], [], 'ro',markersize=6)
    ax.legend() 
    ########################
    def update(frame):
        # Circular motion (cos vs sin)
        X1_traj.set_data(T[:frame], X[:frame])
        X1_dot.set_data([T[frame]], [X[frame]])
        X2_traj.set_data(T[:frame], X2[:frame])
        X2_dot.set_data([T[frame]], [X2[frame]]) 
        return X1_traj, X1_dot, X2_traj, X2_dot 
    ani = animation.FuncAnimation(fig, update, frames=len(T), interval=10, blit=True)
    ani.save('Counpund_Pendulum_simulation.gif', writer='pillow', fps=30)
    plt.tight_layout()
    plt.close()
    #################################################


Create_GIF(t,np.rad2deg(X1P),np.rad2deg(X2P)) 

