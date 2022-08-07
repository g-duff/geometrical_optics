from abc import ABC, abstractmethod
from numpy import array


class ILight(ABC):
    @abstractmethod
    def vectors() -> array:
        pass

