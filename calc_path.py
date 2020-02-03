import OpticalElements as ope
import matplotlib.pyplot as plt
import numpy as np

# Initialize elements
L = ope.lens(10)
fs = ope.free_space(10)
ray = ope.ray(0, np.pi*10/180)

# Create optical path
P = ope.path(fs, L, fs, L, fs)

# Calculate coordinates on optical path
(x_coords, y_coords) = P.calc_coords(ray)

# Plot coordinates
fig, ax = plt.subplots()
ax.plot(x_coords ,y_coords)
ax.grid(True)
ax.set_aspect('equal')
plt.show()
