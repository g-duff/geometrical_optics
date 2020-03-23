import OpticalElements as ope
import matplotlib.pyplot as plt
import numpy as np

# Distance in mm
# 4mm detector
# Treat LEDs as a point source with 10deg divergance


def add_components(ax):

        text_height = ax.get_ylim()[1]*1.2  # Put text 15% above the axes

        ax.axvline(2.5, color='black', ls='--')


        ax.text(2.5, text_height, f'Mirror',
                horizontalalignment='center')

        ax.plot([0, 0], [-1.5, 1.5], color='black', ls='-')
        ax.text(0, text_height, f'Detector',
                horizontalalignment='center')

        ax.plot([5, 5], [-1.5, 1.5], color='black', ls='--')
        ax.text(5, text_height, f'Detector image',
                horizontalalignment='center')

# Units
deg = np.pi/180
mm = 1

# Define LEDs
angle_offset = 0
LED1 = [ope.ray(-5, th*deg+angle_offset) for th in np.linspace(-10, 10, 3)]
LED2 = [ope.ray(5, th*deg-angle_offset) for th in np.linspace(-10, 10, 3)]

# Initialize elements
fs1 = ope.free_space(2.5)
fs2 = ope.free_space(2.5)

# Create optical path
P = ope.path(fs1, fs2)

# Calculate ray coordinates along the path, P
LED1_coords = [P.calc_coords(r) for r in LED1]
LED2_coords = [P.calc_coords(r) for r in LED2]

# Plot rays and lenses
fig, ax = plt.subplots()
for x, y in LED1_coords:
    ax.plot(x, y, color='C0')
for x, y in LED2_coords:
    ax.plot(x, y, color='C1')

# Draw mirror, detector and detector image

add_components(ax)

ax.grid(True)
# ax.set_aspect('equal')

ax.set_xlabel('z (mm)')
ax.set_ylabel('y (mm)')

# Trig calculations

div_angle = 45*deg
det_size = 3

hyp = 5  # mm
op = np.sin(div_angle) * hyp
print(f'The length of the opposite side is {2*op}mm')
print(f'The size of the detector is {det_size}mm')

a1 = [hyp, 1*np.sin(div_angle) * hyp]
a2 = [0, 0]
a3 = [hyp, 1*np.sin(div_angle) * hyp]

x1 = np.array([hyp, 0, hyp])
y1 = np.array([1*np.sin(div_angle) * hyp, 0, -1*np.sin(div_angle) * hyp])

fig2, ax2 = plt.subplots()

ax2.plot(x1, y1+5)

add_components(ax2)

ax2.grid(True)
ax.set_xlabel('z (mm)')
ax.set_ylabel('y (mm)')

plt.tight_layout()
plt.show()
