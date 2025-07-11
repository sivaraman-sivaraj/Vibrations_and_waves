import numpy as np
import matplotlib.pyplot as plt

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

# Time domain from 0 to 10 seconds
t_vals = np.linspace(0, 10, 1000)
y_vals = smooth_random_time_function(t_vals)

# Plot the result
plt.plot(t_vals, y_vals)
plt.title("Smooth Continuous Random Function vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Output f(t)")
plt.ylim(-1.6, 1.6)
plt.grid(True)
plt.show()
