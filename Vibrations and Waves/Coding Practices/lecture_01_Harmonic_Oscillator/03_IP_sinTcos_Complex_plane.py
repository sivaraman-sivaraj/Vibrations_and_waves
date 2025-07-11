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
IP_sin_cos = IP * RP                                    # sin * cos

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
sincos_traj, = ax.plot([], [], 'g-', lw=2, label='IP = sin(ωt)*cos(ωt)')
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
ani.save('Combined_SinCos_vs_Sin_and_Circle.gif', writer='pillow', fps=30)
plt.close()
print("GIF saved as 'Combined_SinCos_vs_Sin_and_Circle.gif'")
