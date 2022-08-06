import unittest
from src.optical_element import IOpticalElement
from numpy import array


class TestIOpticalElement(unittest.TestCase):

    def test_inheritance(self):
        # Given
        # When
        # Then
        assert issubclass(CompleteImplementation, IOpticalElement)
        assert issubclass(IncompleteImplementation, IOpticalElement)

    def test_incomplete_implementation(self):
        # Given
        # When
        try:
            IncompleteImplementation()
            assert False
        # Then
        except TypeError:
            assert True

    def test_complete_implementation(self):
        # Given
        # When
        try:
            CompleteImplementation()
            assert True
        # Then
        except TypeError:
            assert False


class CompleteImplementation(IOpticalElement):
    def matrix(self):
        return array([[1, 0], [0, 1]])


class IncompleteImplementation(IOpticalElement):
    pass
