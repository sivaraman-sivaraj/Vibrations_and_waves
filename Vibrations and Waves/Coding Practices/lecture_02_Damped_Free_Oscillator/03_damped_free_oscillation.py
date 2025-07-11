import os 
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
############################################ 
### Parameters of Pendulum Bar
M   = 10    ## Mass of the pendulum bar
L   = 5     ## Length of the pendulum bar
MoI = (1/3)*M*np.square(L) ## Moment of Inertia of the pendulum bar 
B   = 200     ## Damping Coefficient
############################################ 
g   = 9.81  ## Gravitational acceleration
phi = 0.0   ## phase delay
Theta_degree  = 30 
Theta_initial = np.deg2rad(Theta_degree)
Omega_0 = np.sqrt(3*g/(2*L)) 
Gamma   = (3*B)/(M*np.square(L))
print("The natural frequency of pendulum bar : ",str(Omega_0)) 
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

system_id = How_is_is_damped(Omega_0,Gamma)
#############################################
########## Under Damped System ##############
############################################# 
def Underdamped():
    omega = np.square(Omega_0) - (np.square(Gamma)/4) 
    phi   = np.arctan(-Gamma/(2*omega))
    A     = Theta_initial/np.cos(phi) 
    ### simulation 
    t = np.linspace(0, 20, 2000)
    Theta_t = A*np.cos((omega*t)+phi)*np.exp(-0.5*Gamma*t) 
    plt.figure(figsize=(12,5)) 
    plt.plot(t,np.rad2deg(Theta_t),color="teal",linewidth=2.0) 
    plt.grid(True) 
    plt.xlabel("Time (in seconds)") 
    plt.ylabel("Theta (in degree)") 
    plt.title("System with Near to Critical damped conidtion")
    plt.axhline(y=0,color="grey",linewidth=2.0) 
    plt.axvline(x=0,color="grey",linewidth=2.0) 
    plt.savefig("Pendulum_bar_2d.jpg",dpi=420)
    plt.show() 
    return t,np.rad2deg(Theta_t)

def Complex_underdamped():
    omega = np.square(Omega_0) - (np.square(Gamma)/4) 
    phi   = np.arctan(-Gamma/(2*omega))
    A     = Theta_initial/np.cos(phi) 
    ### simulation 
    t = np.linspace(0, 20, 2000)
    RP = A*np.cos((omega*t)+phi)*np.exp(-0.5*Gamma*t) 
    IP = A*np.sin((omega*t)+phi)*np.exp(-0.5*Gamma*t) 
    #### 
    plt.figure(figsize=(8,8)) 
    plt.plot(RP,IP,color="crimson",linewidth=2.0) 
    plt.scatter(RP[::20],IP[::20],marker="o",color="m",alpha=0.2) 
    plt.xlabel("Real Part") 
    plt.ylabel("Imaginary Part") 
    plt.title("Pendulum Bar") 
    plt.grid(True) 
    plt.savefig("Pendulum_Complex_2d.jpg",dpi=320)
    plt.show() 
    return np.rad2deg(RP),np.rad2deg(IP) 

def Overdamped():
    omega = np.square(Omega_0) - (np.square(Gamma)/4) 
    phi   = np.arctan(-Gamma/(2*omega))
    A     = Theta_initial/np.cos(phi) 
    ### simulation 
    t = np.linspace(0, 20, 2000)
    G_p = (Gamma/2) + np.sqrt((np.square(Gamma)/4)-np.square(Omega_0)) 
    G_m = (Gamma/2) - np.sqrt((np.square(Gamma)/4)-np.square(Omega_0)) 
    A_p = Theta_initial/(1-(G_p/G_m)) 
    A_m = Theta_initial/(1-(G_m/G_p)) 
    Theta_t =  (A_p*np.exp(-G_p*t)) + (A_m*np.exp(-G_m*t)) 
    plt.figure(figsize=(12,5)) 
    plt.plot(t[:500],np.rad2deg(Theta_t)[:500],color="teal",linewidth=2.0) 
    plt.grid(True) 
    plt.xlabel("Time (in seconds)") 
    plt.ylabel("Theta (in degree)") 
    plt.title("System with Over damped conidtion")
    plt.axhline(y=0,color="navy",linewidth=2.0) 
    plt.axvline(x=0,color="navy",linewidth=2.0) 
    plt.savefig("Pendulum_bar_2d.jpg",dpi=420)
    plt.show() 
    return t,np.rad2deg(Theta_t)



def Create_GIF(T,X):
    fig,ax = plt.subplots(figsize=(12,5)) 
    ax.set_xlim(T[0] - 0.2, T[-1] + 0.2)
    ax.set_ylim(-32, 32) ## <-- pay attention here..!
    ax.set_title("The System's amplitude in time domain")
    ax.set_xlabel("Time (in Seconds)")
    ax.set_ylabel("Amplitude (in degree)")
    ax.grid()
    ########################
    Angle_traj, = ax.plot([], [], 'teal', lw=4, label='Pendulum Bar')
    Angle_dot,  = ax.plot([], [], 'ro',markersize=6) 
    ax.legend() 
    ########################
    def update(frame):
        # Circular motion (cos vs sin)
        Angle_traj.set_data(T[:frame], X[:frame])
        Angle_dot.set_data([T[frame]], [X[frame]])
        return Angle_traj, Angle_dot 
    ani = animation.FuncAnimation(fig, update, frames=len(T), interval=10, blit=True)
    ani.save('Pendulum_bar_simulation.gif', writer='pillow', fps=30)
    plt.close()
    #################################################



def Create_Complex_GIF(RP,IP):
    fig,ax = plt.subplots(figsize=(8,8)) 
    ax.set_xlim(-Theta_degree-2, Theta_degree + 2)
    ax.set_ylim(-Theta_degree-2, Theta_degree+2) ## <-- pay attention here..!
    ax.set_title("The System's amplitude in complex domain")
    ax.set_xlabel("Real part (in degree)")
    ax.set_ylabel("Imaginary part (in degree)")
    ax.axhline(y=0,color="k") 
    ax.axvline(x=0,color="k")
    ax.grid()
    ########################
    Angle_traj, = ax.plot([], [], 'teal', lw=4, label='Pendulum Bar')
    Angle_dot,  = ax.plot([], [], 'ro',markersize=6) 
    ax.legend() 
    ########################
    def update(frame):
        # Circular motion (cos vs sin)
        Angle_traj.set_data(RP[:frame], IP[:frame])
        Angle_dot.set_data([RP[frame]], [IP[frame]])
        return Angle_traj, Angle_dot 
    ani = animation.FuncAnimation(fig, update, frames=len(RP), interval=20, blit=True)
    ani.save('Pendulum_bar_Complex_sim.gif', writer='pillow', fps=30)
    plt.close()
    #################################################

def Simulate_system(id):
    if id == 1:
        t,Theta_t = Underdamped() 
    elif id==3:
        t,Theta_t = Overdamped()
    return t,Theta_t
#############################################
#############################################
TT,XX = Simulate_system(system_id)
# QQ,RR = Complex_underdamped()
# Create_GIF(TT,XX)
# Create_Complex_GIF(QQ,RR) 
#############################################
#############################################

