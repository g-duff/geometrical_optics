import unittest
from src.optical_element import IOpticalElement, FreeSpace
from numpy import array, array_equal


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


class TestFreeSpace(unittest.TestCase):

    def test_is_optical_element(self):
        # Given
        # When
        # Then
        assert issubclass(FreeSpace, IOpticalElement)

    def test_matrix(self):
        # Given
        length = 10
        free_space = FreeSpace(length)

        expected_free_space_matrix = array([[1, length], [0, 1]])

        # When
        actual_free_space_matrix = free_space.matrix()

        # Then
        assert array_equal(expected_free_space_matrix,
                           actual_free_space_matrix)
