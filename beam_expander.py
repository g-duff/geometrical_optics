import OpticalElements as ope
import matplotlib.pyplot as plt
import numpy as np

# Define point source
rays = [ope.ray(th, 0) for th in np.linspace(-10, 10, 10)]

# Initialize elements
fs1 = ope.free_space(10)
fs2 = ope.free_space(20)
L1 = ope.lens(10)
L2 = ope.lens(20)

# Create optical path
P = ope.path(fs1, L1, fs1, fs2, L2, fs2)

# Calculate ray coordinates along the path, P
coords_list = [P.calc_coords(r) for r in rays]

# Plot rays and lenses
fig, ax = plt.subplots()
for x, y in coords_list: ax.plot(x, y, color='C0')
P.plot_lenses(ax)

ax.grid(True)
ax.set_aspect('equal')
plt.show()
