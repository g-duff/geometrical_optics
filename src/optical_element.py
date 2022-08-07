from abc import ABC, abstractmethod
from numpy import array


class IOpticalElement(ABC):
    @abstractmethod
    def matrix(self) -> array:
        pass


class FreeSpace(IOpticalElement):
    def __init__(self, length: float):
        ''' Free space

        length: length of the free space'''
        self.length = length

    def matrix(self) -> array:
        return array([[1, self.length], [0, 1]])


class Lens(IOpticalElement):
    def __init__(self, focal_length: float):
        ''' A lens

        focal_length: focal length of the lens'''
        self.focal_length = focal_length

    def matrix(self) -> array:
        return array([[1, 0], [-1/self.focal_length, 1]])
