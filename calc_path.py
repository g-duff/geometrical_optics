import OpticalElements as ope
import matplotlib.pyplot as plt
import numpy as np

# Initialize elements
fs = ope.free_space(10)
L1 = ope.lens(10)
L2 = ope.lens(20)

ray_1 = ope.ray(3, np.pi*10/180)
ray_2 = ope.ray(-3, -np.pi*10/180)
ray_3 = ope.ray(0, 0)

rays = [ray_1, ray_2, ray_3]

# Create optical path
P = ope.path(fs, L1, fs, L2, fs, fs)

# Calculate coordinates on optical path
fig, ax = plt.subplots()

P.plot_lenses(ax)

# Calculate and plot coordinates
coords_list = [(P.calc_coords(r)) for r in rays]
for x, y in coords_list: ax.plot(x, y, color='C0')

ax.grid(True)
ax.set_aspect('equal')
plt.show()
