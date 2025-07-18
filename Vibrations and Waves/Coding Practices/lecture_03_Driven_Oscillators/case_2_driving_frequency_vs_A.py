import os 
import numpy as np
import scipy as sp 
import matplotlib.pyplot as plt 
################################################################ 
############ Physical Parameters of Pendulum Bar ###############
################################################################
# M   = 1    ## Mass of the pendulum bar
# L   = 1     ## Length of the pendulum bar
# MoI = (1/3)*M*np.square(L) ## Moment of Inertia of the pendulum bar 
# B   = 1   ## Damping Costant
# ################################################################
# ##################### System Parameters ########################
# ################################################################
# g             = 9.81  ## Gravitational acceleration
# phi           = 0.0   ## phase delay
# Theta_initial = np.deg2rad(0)
# ## Natural frequency of the pendulum bar
# Omega_0       = np.sqrt(3*g/(2*L))  
# ## Damping constant 
# Gamma         = 3*B/(M*np.square(L))  # Damping Coefficient
# ## Net frequency 
# Omega         = np.sqrt(np.square(Omega_0) - (np.square(Gamma)/4))  
# ## input parameters
# d             = 50 ## torque amplitude 
# f0            = d/MoI
# f             = 0.5  ## frequency of the periodic driving force 
# Omega_d       = np.linspace(0,(2*np.pi),2000)##2*np.pi*f ## driving frequency
################################################################
##################### Governing Equation #######################
################################################################ 
### standard one plot
def Calculate_Aw(OD,f0,Omega_0,Gamma):
    A_wd       = f0/np.sqrt(np.square(np.square(Omega_0) - np.square(OD))+(np.square(OD)*np.square(Gamma))) 
    return A_wd

# A_wd_List = []
# for i in range(len(Omega_d)):
#     w_temp = Omega_d[i] 
#     A_wd_List.append(Calculate_Aw(w_temp)) 

# plt.figure(figsize=(9,6))
# plt.plot(Omega_d,A_wd_List,color="navy",linestyle="--",linewidth=2.0,label="For Mass=1, Length=1, B (damping constant)=1") 
# plt.xlabel("Driving Frequency (in rad/s)")
# plt.ylabel("Damping Factor") 
# plt.title("Driving Frequency ($\omega_d$) Value of Pi")
# plt.grid()  
# plt.legend(loc="best") 
# plt.savefig("Sim_02_Driving_Frequency_vs_Damping_Factor_baseline.jpg",dpi=360)
# plt.show() 
Omega_d       = np.linspace(0,(2*np.pi),2000)##2*np.pi*f ## driving frequency
################################################################ 
################################################################ 
def Damping_Constant_Simulation(BB):
    M   = 1    ## Mass of the pendulum bar
    L   = 1     ## Length of the pendulum bar
    MoI = (1/3)*M*np.square(L) ## Moment of Inertia of the pendulum bar  
    ######################################################################
    g             = 9.81  ## Gravitational acceleration
    phi           = 0.0   ## phase delay
    Theta_initial = np.deg2rad(0)
    ## Natural frequency of the pendulum bar
    Omega_0       = np.sqrt(3*g/(2*L))  
    ## Damping constant 
    Gamma         = 3*BB/(M*np.square(L))  # Damping Coefficient
    ## Net frequency 
    Omega         = np.sqrt(np.square(Omega_0) - (np.square(Gamma)/4))  
    ## input parameters
    d             = 50 ## torque amplitude 
    f0            = d/MoI
    f             = 0.5  ## frequency of the periodic driving force 
    Omega_d       = np.linspace(0,(2*np.pi),2000)##2*np.pi*f ## driving frequency
    ###############################################
    A_wd_List = []
    for i in range(len(Omega_d)):
        w_temp = Omega_d[i] 
        A_wd_List.append(Calculate_Aw(w_temp,f0,Omega_0,Gamma))  

    Q = Omega_0/Gamma
    return A_wd_List, Q 

AWL = []
BBL = [0.01,0.5,1,5,10,40] 
Q_C = []
Complex_C = []
for i1 in BBL:
    b_temp = i1 
    try:
        print(b_temp)
        Aw_temp, Q_temp = Damping_Constant_Simulation(b_temp) 
        AWL.append(Aw_temp) 
        Q_C.append(Q_temp) 
        print(len(Aw_temp))

    except ValueError as e:
        Complex_C.append(b_temp)


plt.figure(figsize=(9,6)) 
for jj in range(len(AWL)):
    q_value = Q_C[jj]
    plt.plot(Omega_d,AWL[jj],linewidth=2.0) 
    plt.annotate(f'Q={q_value:.2f}',xy=(Omega_d[900],AWL[jj][900]),xytext=(Omega_d[900],AWL[jj][900]))

plt.xlabel("Driving Frequency ($\omega_d$/s)")
plt.ylabel("Damping Factor ($A(\omega_d)$)") 
plt.grid()  
plt.ylim(-1,30)
plt.title("System responses for Various Q = ($\omega_0$ / $\Gamma$) Values")
plt.savefig("sim_03_Q_Comparison.jpg", dpi=360)
plt.show() 










    
