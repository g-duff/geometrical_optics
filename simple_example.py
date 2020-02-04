import OpticalElements as ope
import matplotlib.pyplot as plt
import numpy as np

# Initialize elements
fs = ope.free_space(10)
L = ope.lens(10)

# Define ray 0mm above the optic axis at an angle of 10deg
ray = ope.ray(0, 10*np.pi/180)

# Create optical path
P = ope.path(fs, L, fs)

# Calculate ray coordinates along the path, P
x_coords, y_coords = P.calc_coords(ray)

# Plot rays and lenses
fig, ax = plt.subplots()
ax.plot(x_coords, y_coords, color='C0')
P.plot_lenses(ax)

ax.grid(True)
ax.set_aspect('equal')
plt.show()
