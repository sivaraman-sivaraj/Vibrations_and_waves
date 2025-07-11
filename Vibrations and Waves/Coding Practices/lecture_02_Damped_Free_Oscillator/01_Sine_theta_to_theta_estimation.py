import os 
import numpy as np 
import matplotlib.pyplot as plt 
#######################################################################
############## Taylor Series on Sin(theta) = Theta ####################
### on expansion
### f(x) = f(x)+ f'(x)*x/1! + f''(x)*x^2/2! + f'''(x)*x^3/3!+.......
#######################################################################
theta     = np.deg2rad(np.arange(0,90)) 
sin_theta = np.sin(theta)

def Taylor_Series_App(ST,T):
    V = (ST) - ((ST**3)/6) - ((ST**5)/120) ## we are stopping our approximation at power of 5 
    return V/T
#######################################
Deviation = []
for i in range(len(theta)):
    try:
        _ = sin_theta[i]/theta[i]
        temp = Taylor_Series_App(sin_theta[i],theta[i]) # sin_theta[i]/theta[i]
        Deviation.append(temp)
    except ZeroDivisionError:
        temp = Taylor_Series_App(sin_theta[i],1)   # sin_theta[i] 
        Deviation.append(temp)  

Deviation    = Deviation*100
Deviation[0] = 1 
#######################################################################
#######################################################################
NN = 18
NB = [str(i) for i in range(0,90)]
# bars = plt.bar(NB[:NN],Deviation[:NN], color='skyblue')
# Create bar plot
plt.figure(figsize=(12,5))
bars = plt.bar(NB[:NN], Deviation[:NN], color='grey',alpha=0.5)
plt.scatter(NB[:NN], Deviation[:NN], color='olive')
plt.title('Approximation of sin(t)/t')
plt.xlabel('Theta (degree)')
#######
### Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x position
        height,                             # y position (top of bar)
        f'{round(height*100,2)}',                        # label
        ha='center', va='bottom'            # horizontal and vertical alignment
    ) 
#######
plt.ylabel('Percentage')
plt.axhline(y=1,color="black")
plt.axvline(x=0,color="black")
plt.ylim(0.75,1.05)
plt.grid(True, linestyle='--', alpha=0.5) 
plt.savefig("sin_theta_equal_to_theta.jpg", dpi=300, bbox_inches='tight')
plt.show()
#########################################################
#########################################################




# print(sin_theta)
# ss = np.sin(90) 
# dd = np.sin(np.deg2rad(90)) 



