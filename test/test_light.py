import unittest
from src.light import ILight, Ray
from numpy import array, array_equal


class TestIOpticalElement(unittest.TestCase):

    def test_inheritance(self):
        # Given
        # When
        # Then
        assert issubclass(CompleteImplementation, ILight)
        assert issubclass(IncompleteImplementation, ILight)

    def test_complete_implementation(self):
        # Given
        # When
        try:
            CompleteImplementation()
            assert True
        # Then
        except TypeError:
            assert False

    def test_incomplete_implementation(self):
        # Given
        # When
        try:
            IncompleteImplementation()
            assert False
        # Then
        except TypeError:
            assert True


class CompleteImplementation(ILight):
    def vectors(self):
        return array([[1, 0], [0, 1]])


class IncompleteImplementation(ILight):
    pass


class TestRay(unittest.TestCase):

    def test_vectors(self):
        # Given
        height_above_optical_axis = 10
        angle_to_optical_axis = 0.1
        ray = Ray(height_above_optical_axis, angle_to_optical_axis)
        expected_vectors = array(
            [height_above_optical_axis, angle_to_optical_axis])

        # When
        actual_vectors = ray.vectors()

        # Then
        assert array_equal(expected_vectors, actual_vectors)
