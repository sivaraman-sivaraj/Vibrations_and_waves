import os 
import numpy as np 
import scipy as sp
import matplotlib.pyplot as plt
################################################
################################################

def Driving_Coefficients(wd,F0=1):
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
    ## Applying cramer's rule to find B value 

    ## B11 
    B1M = np.array([[D11,A12],[D21,A22]]) 
    B2M = np.array([[A11,D11],[A21,D21]]) 

    B11 = np.linalg.det(B1M)/np.linalg.det(E) 
    B21 = np.linalg.det(B2M)/np.linalg.det(E) 
    return B11,B21,w1,w2 
################################################
################################################ 
wL = np.linspace(0,2*np.pi,1200) 

B1,B2 = [],[] 
for i in range(len(wL)):
    wd_temp  = wL[i]
    try:
        b1_temp,b2_temp,omega_1,omega_2 = Driving_Coefficients(wd_temp) 
        B1.append(b1_temp) 
        B2.append(b2_temp) 
    except ZeroDivisionError:
        S = 0

##############################################
############################################## 
plt.figure(figsize=(9,6)) 
plt.plot(wL,B1,color="navy",linewidth=2.0,label="B1") 
plt.plot(wL,B2,color="teal",linewidth=2.0,label="B2")
plt.xlabel("Driving Frequency (rad/s)") 
plt.ylabel("B- Coefficient") 
plt.grid() 
plt.axvline(x=omega_1,color="coral",linewidth=2.0) 
plt.axvline(x=omega_2,color="coral",linewidth=2.0) 
plt.axhline(y=0,color="grey",linewidth=2.0) 
plt.title("Why driving frequency ($\omega_d$) matters ?")
plt.xlim(2.2,3.6) 
plt.ylim(-4,4)
plt.legend(loc="best") 
w1_text = '$\omega_1$ = '+str(round(omega_1,3)) 
w2_text = '$\omega_2$ = '+str(round(omega_2,3))
plt.annotate(w1_text, 
             xy=(omega_1, 2),             # Point to annotate
             xytext=(2.7, 2.5),     # Position of the text
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12,
             color='blue')
plt.annotate(w2_text, 
             xy=(omega_2, 2),             # Point to annotate
             xytext=(3.3, 2.5),     # Position of the text
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12,
             color='blue') 
plt.text(3.2, -2, "Compound Pendulum : 1\n K= 5 N/m 2\n M = 3 kg 3\n L = 1.2m" )
plt.savefig("Driving_Frequency_Analysis.jpg",dpi=360)
plt.show() 
##############################################
############################################## 




