import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
alpha = np.radians(30)  # Incline angle in radians
m = 1.0  # Mass of the objects (kg)
r = 0.1  # Radius of the objects (m)
t_max = 10  # Total time of the simulation (s)
dt = 0.01  # Time step (s)

# Moments of inertia for sphere (I_b) and cylinder (I_d)
I_b = (2/5) * m * r**2
I_d = (1/2) * m * r**2

# Midpoint method function
def midpoint_method(f, y0, t):
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(len(t) - 1):
        y_half = y[i] + f(y[i], t[i]) * dt/2
        y[i + 1] = y[i] + f(y_half, t[i] + dt/2) * dt
    return y

# Equations of motion for the sphere and cylinder
def rolling_sphere(y, t):
    ds_dt = y[1]
    a = g * np.sin(alpha) / (1 + I_b / (m * r ** 2))
    dv_dt = a
    return np.array([ds_dt, dv_dt])


def rolling_cylinder(y, t):
    ds_dt = y[1]
    a = g * np.sin(alpha) / (1 + I_d / (m * r ** 2))
    dv_dt = a
    return np.array([ds_dt, dv_dt])
# Initial conditions
initial_conditions = [0, 0]  # Starting at s=0 and v=0

# Time array
t = np.arange(0, t_max, dt)

# Perform the simulations
results_sphere = midpoint_method(rolling_sphere, initial_conditions, t)
results_cylinder = midpoint_method(rolling_cylinder, initial_conditions, t)

# Extracting the results
s_sphere = results_sphere[:, 0]
v_sphere = results_sphere[:, 1]
s_cylinder = results_cylinder[:, 0]
v_cylinder = results_cylinder[:, 1]

# Plotting
plt.figure(figsize=(12, 6))

# Position (center of mass) plot
plt.subplot(2, 1, 1)
plt.plot(t, s_sphere, label='Sphere')
plt.plot(t, s_cylinder, label='Cylinder')
plt.title('Position and Velocity of Rolling Objects')
plt.ylabel('Position (m)')
plt.legend()

# Velocity plot
plt.subplot(2, 1, 2)
plt.plot(t, v_sphere, label='Sphere')
plt.plot(t, v_cylinder, label='Cylinder')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()

plt.tight_layout()
plt.show()
