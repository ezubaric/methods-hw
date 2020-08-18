
import unittest
import numpy as np

from matrix_multiply import matrix_multiply, DimensionError

class TestMatrixMultiply(unittest.TestCase):
    def test_dimension(self):
        left = np.array([[1, 2], [3, 4]])
        right = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        with self.assertRaises(Exception):  matrix_multiply(left, right)

    def test_dot(self):
        left = np.array([[1, 0, 2]])
        right = np.array([[5], [0], [3]])

        np.testing.assert_array_equal(np.array([[11]]), matrix_multiply(left, right))

    def test_identity(self):
        left = np.array([[1, 0], [0, 1]])
        right = np.array([[5, 2], [3, 4]])

        np.testing.assert_array_equal(right, matrix_multiply(left, right))

    def test_uneven(self):
        left = np.array([[2, 0, 4], [0, 8, 0]])
        right = np.array([[1], [0], [3]])

        np.testing.assert_array_equal(np.array([[14], [0]]), matrix_multiply(left, right))

if __name__ == '__main__':
    unittest.main()
