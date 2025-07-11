import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
############################################
# Smooth random-like function over time [0, 10]
def smooth_random_time_function(t):
    # Combine sinusoids with different frequencies and phases
    y = (
        0.6 * np.sin(2 * np.pi * 0.5 * t + 0.8) +
        0.5 * np.sin(2 * np.pi * 1.1 * t - 1.3) +
        0.4 * np.sin(2 * np.pi * 2.3 * t + 2.2)
    )
    # Normalize output to [-1.5, 1.5]
    y = (y / np.max(np.abs(y))) * 1.5
    return y
##############################################
# System parameters
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# System parameters
K = 10
M = 15
X_initial = 1.5

omega_0 = np.sqrt(K / M)
print("Natural frequency:", round(omega_0, 4))

t = np.linspace(0, 10, 1000)
phi = np.deg2rad(0)

# Signals
RP = X_initial * np.cos(omega_0 * t + phi)              # Real part (cos)
IP = X_initial * np.sin(omega_0 * t + phi)              # Imag part (sin)
IP_sin_cos = smooth_random_time_function(t) # IP * RP                                    # sin * cos

# Setup a single plot
fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim(-X_initial - 0.2, X_initial + 0.2)
ax.set_ylim(-X_initial-0.2, X_initial+0.2)
ax.set_title("Complex Representation")
ax.set_xlabel("Real Part")
ax.set_ylabel("Imaginary Part")
ax.grid()

# Circular trajectory (cos vs sin)
circle_traj, = ax.plot([], [], 'b-', lw=2, label='IP = sin(ωt)')
circle_dot, = ax.plot([], [], 'ro')

# sin*cos vs sin
sincos_traj, = ax.plot([], [], 'g-', lw=2, label='IP = random function')
sincos_dot, = ax.plot([], [], 'ko')

ax.legend()

# Animation update
def update(frame):
    # Circular motion (cos vs sin)
    circle_traj.set_data(RP[:frame], IP[:frame])
    circle_dot.set_data([RP[frame]], [IP[frame]])

    # sin*cos vs sin
    sincos_traj.set_data(RP[:frame], IP_sin_cos[:frame])
    sincos_dot.set_data([RP[frame]], [IP_sin_cos[frame]])

    return circle_traj, circle_dot, sincos_traj, sincos_dot

# Animate
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=10, blit=True)

# Save GIF
ani.save('Random_IP.gif', writer='pillow', fps=30)
plt.close()
print("GIF saved as 'Random_IP.gif'")
