from abc import ABC, abstractmethod
from numpy import array


class ILight(ABC):
    @abstractmethod
    def vectors() -> array:
        pass


class Ray(ILight):
    def __init__(self, height_above_optical_axis: float, angle_to_optical_axis: float):
        ''' A ray of light

        height_above_optical_axis
        angle_to_optical_axis: in radians'''
        self.height_above_optical_axis = height_above_optical_axis
        self.angle_to_optical_axis = angle_to_optical_axis

    def vectors(self) -> array:
        return array([self.height_above_optical_axis, self.angle_to_optical_axis])
