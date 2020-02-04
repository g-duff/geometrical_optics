import numpy as np

class lens:
    def __init__(self, f):
        ''' A lens.
        f: focal length'''
        self.f = f
        self.matrix = np.array([[1, 0],[-1/f, 1]])

class free_space:
    def __init__(self, l):
        ''' Free space.
        l: length'''
        self.l = l
        self.matrix = np.array([[1, l],[0, 1]])

class ray:
    def __init__(self, r, theta):
        ''' A ray
        r: height above axis
        theta: angle of ray in radians'''
        self.r = r
        self.theta = theta
        self.vector = np.array([r,theta])

class path:
    def __init__(self, *elements):
        ''' An optical path with a variable number
        of elements.
        elements: A sequence of optical elements through which the ray passes'''
        self.elements = [free_space(0)]+list(elements)

    def append(self, element):
        ''' Append an optical element to the end of the optical path'''
        self.elements.append(element)

    def calc_coords(self, ray):
        ''' Calculate the x and y coords for the optical path
        ray: an OpticalElements ray

        x_coords: a list of x coordinates along the optical path
        y_coords: a list of y coordinates along the optical path'''
        return self.calc_x_coords(), self.calc_y_coords(ray)

    def calc_x_coords(self):
        ''' Calculate the x and y coords for the optical path
        ray: an OpticalElements ray

        x_coords: a list of x coordinates along the optical path'''
        x_coords = [e.matrix[0,1] for e in self.elements]
        x_coords = np.cumsum(x_coords)
        return x_coords

    def calc_y_coords(self, ray):
        ''' Calculate the x and y coords for the optical path
        ray: an OpticalElements ray

        y_coords: a list of y coordinates along the optical path'''
        new_ray = np.array([1,1])*ray.vector
        y_coords = []
        for e in self.elements:
            new_ray = e.matrix@new_ray
            y_coords.append(new_ray[0])
        return y_coords

    def plot_lenses(self, ax):
        ''' Represents lenses as dashed lines,
        labeled with their focal lengths

        Call after plotting rays'''
        text_height = ax.get_ylim()[1]*1.2 # Put text 15% above the axes

        for x, e in zip(self.calc_x_coords(), self.elements):
            if type(e)==lens:
                ax.axvline(x, color='black', ls='--')
                ax.text(x, text_height, f'f={e.f}mm', \
                    horizontalalignment='center')
