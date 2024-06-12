import matplotlib.pyplot as plt
import numpy as np

GRAVITATIONAL_CONSTANT = 6.6743e-11
MASS_SUN = 1.989e30
MASS_EARTH = 5.972e24
MASS_MOON = 7.347e22
DISTANCE_EARTH_SUN = 1.5e11
DISTANCE_EARTH_MOON = 384400e3

def simulate_orbital_motion(initial_velocity, total_time, time_step, gravitational_constant, central_mass, initial_distance):
    num_steps = int(total_time / time_step)
    positions = np.zeros((num_steps + 1, 2))
    velocities = np.zeros((num_steps + 1, 2))

    positions[0] = [0, initial_distance]
    velocities[0] = [initial_velocity, 0]

    for i in range(num_steps):
        distances = np.linalg.norm(positions[i])
        acceleration = -(gravitational_constant * central_mass / distances**3) * positions[i]
        velocities[i + 1] = velocities[i] + acceleration * time_step
        positions[i + 1] = positions[i] + velocities[i] * time_step + 0.5 * acceleration * time_step**2

    return positions[:, 0], positions[:, 1]

moon_velocity = np.sqrt(GRAVITATIONAL_CONSTANT * MASS_EARTH / DISTANCE_EARTH_MOON)
earth_velocity = np.sqrt(GRAVITATIONAL_CONSTANT * MASS_SUN / DISTANCE_EARTH_SUN)
simulation_time = 24 * 365.25 * 3600
time_step = 7200

moon_path_x, moon_path_y = simulate_orbital_motion(moon_velocity, simulation_time, time_step, GRAVITATIONAL_CONSTANT, MASS_EARTH, DISTANCE_EARTH_MOON)
earth_path_x, earth_path_y = simulate_orbital_motion(earth_velocity, simulation_time, time_step, GRAVITATIONAL_CONSTANT, MASS_SUN, DISTANCE_EARTH_SUN)


scaled_earth_path_x = earth_path_x / 10
scaled_earth_path_y = earth_path_y / 10


relative_moon_path_x = moon_path_x + scaled_earth_path_x
relative_moon_path_y = moon_path_y + scaled_earth_path_y

plt.plot(scaled_earth_path_x, scaled_earth_path_y, label='Earth Orbit')
plt.plot(relative_moon_path_x, relative_moon_path_y, label='Moon Orbit')
plt.legend()
plt.show()
