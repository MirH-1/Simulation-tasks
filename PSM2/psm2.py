import matplotlib.pyplot as plt
import numpy as np

m = 1.0
g = 9.81
k = 0.5

angle = 45.0
v0 = 100.0
t_max = 20.0
dt = 0.1

angle_rad = np.radians(angle)

x0 = 0.0
y0 = 0.0
vx0 = v0 * np.cos(angle_rad)
vy0 = v0 * np.sin(angle_rad)

def acceleration(vx, vy):
    Fd_x = -k * vx
    Fd_y = -k * vy
    ax = Fd_x / m
    ay = (Fd_y / m) - g
    return ax, ay

def eulers_method(x0, y0, vx0, vy0, t_max, dt):
    x = [x0]
    y = [y0]
    vx = [vx0]
    vy = [vy0]

    while y[-1] >= 0:
        ax, ay = acceleration(vx[-1], vy[-1])
        vx.append(vx[-1] + ax * dt)
        vy.append(vy[-1] + ay * dt)
        x.append(x[-1] + vx[-1] * dt)
        y.append(y[-1] + vy[-1] * dt)

    return np.array(x), np.array(y)

def improved_eulers_method(x0, y0, vx0, vy0, t_max, dt):
    x = [x0]
    y = [y0]
    vx = [vx0]
    vy = [vy0]

    while y[-1] >= 0:
        ax, ay = acceleration(vx[-1], vy[-1])
        est_vx = vx[-1] + ax * dt
        est_vy = vy[-1] + ay * dt
        est_ax, est_ay = acceleration(est_vx, est_vy)
        avg_ax = (ax + est_ax) / 2
        avg_ay = (ay + est_ay) / 2
        vx.append(vx[-1] + avg_ax * dt)
        vy.append(vy[-1] + avg_ay * dt)
        x.append(x[-1] + vx[-1] * dt)
        y.append(y[-1] + vy[-1] * dt)

    return np.array(x), np.array(y)

x_euler, y_euler = eulers_method(x0, y0, vx0, vy0, t_max, dt)
x_improved, y_improved = improved_eulers_method(x0, y0, vx0, vy0, t_max, dt)

plt.figure(figsize=(12, 6))
plt.plot(x_euler, y_euler, label='Euler Method')
plt.plot(x_improved, y_improved, label='Improved Euler Method', linestyle='--')
plt.xlabel('DISTANCE (m) ')
plt.ylabel('HEIGHT(m)')
plt.title('Euler vs. Improved Euler')
plt.legend()
plt.grid(True)
plt.show()
