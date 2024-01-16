import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz system equations
def lorenz_system(x, y, z, sigma=10, rho=28, beta=8/3):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return dx, dy, dz

def integrate_lorenz(initial_state, dt, steps):
    x, y, z = initial_state
    trajectory = np.zeros((steps, 3))

    for i in range(steps):
        trajectory[i] = [x, y, z]
        dx, dy, dz = lorenz_system(x, y, z)
        x += dt * dx
        y += dt * dy
        z += dt * dz

    return trajectory

# Set initial conditions
initial_state = [0.1, 0.0, 0.0]
dt = 0.01
steps = 10000

# Integrate the Lorenz system
trajectory = integrate_lorenz(initial_state, dt, steps)

# Plotting the 3D trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2])

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Lorenz System 3D Trajectory')

plt.show()
