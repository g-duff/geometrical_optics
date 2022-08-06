from abc import ABC, abstractmethod
from numpy import array

class IOpticalElement(ABC):
    @abstractmethod
    def matrix(self) -> array:
        pass

