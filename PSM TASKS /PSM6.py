import numpy as np
import matplotlib.pyplot as plt


def simulate_string_motion(L, N, dt, total_time):
    dx = L / N
    x = np.linspace(0, L, N + 1)
    y = np.sin(x)  
    v = np.zeros(N + 1)

    ek = []
    ep = []
    et = []

    for t in np.arange(0, total_time, dt):

        a = np.zeros(N + 1)
        for i in range(1, N):
            a[i] = (y[i - 1] - 2 * y[i] + y[i + 1]) / dx ** 2


        y_mid = y + 0.5 * dt * v
        v_mid = v + 0.5 * dt * a


        a_mid = np.zeros(N + 1)
        for i in range(1, N):
            a_mid[i] = (y_mid[i - 1] - 2 * y_mid[i] + y_mid[i + 1]) / dx ** 2

        # Calculate full step
        y += dt * v_mid
        v += dt * a_mid


        y[0], y[-1] = 0, 0


        ek.append(0.5 * np.sum(v ** 2) * dx)
        ep.append(0.5 * np.sum((y[1:] - y[:-1]) ** 2) / dx)
        et.append(ek[-1] + ep[-1])

    return ek, ep, et



L = np.pi
N = 10
dt = 0.2
total_time = 3

ek, ep, et = simulate_string_motion(L, N, dt, total_time)


plt.figure(figsize=(10, 6))
plt.plot(ek, label='Kinetic Energy (Ek)', marker='o')
plt.plot(ep, label='Potential Energy (Ep)', marker='x')
plt.plot(et, label='Total Energy (Et)', marker='^')
plt.title('Energy of the Vibrating String Over Time')
plt.xlabel('Time step')
plt.ylabel('Energy')
plt.legend()
plt.show()