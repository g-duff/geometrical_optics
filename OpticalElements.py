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

        self.S = S = np.eye(2)
        x_coords = [e.matrix[0,1] for e in self.elements]
        x_coords = np.cumsum(x_coords)

        y_coords = []

        new_ray = np.array([1,1])
        new_ray = new_ray*ray.vector
        for e in self.elements:
            new_ray = e.matrix@new_ray
            y_coords.append(new_ray[0])

        return x_coords, y_coords

    def plot_ray(self, ax):
        pass
