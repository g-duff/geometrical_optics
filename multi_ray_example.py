import OpticalElements as ope
import matplotlib.pyplot as plt
import numpy as np

# Initialize elements
fs = ope.free_space(10)
L1 = ope.lens(10)
L2 = ope.lens(10)

# Define rays
rays = [ope.ray(0, np.pi*th/180) for th in np.linspace(-10, 10, 10)]

# Create optical path
P = ope.path(fs, L1, fs, L2, fs, fs)

# Calculate ray coordinates along the path, P
coords_list = [P.calc_coords(r) for r in rays]

# Plot rays and lenses
fig, ax = plt.subplots()
for x, y in coords_list: ax.plot(x, y, color='C0')
P.plot_lenses(ax)

ax.grid(True)
ax.set_aspect('equal')
plt.show()
