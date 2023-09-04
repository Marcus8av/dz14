import unittest
from matrix import Matrix

class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.matrix1 = Matrix([[1, 2], [3, 4]])
        self.matrix2 = Matrix([[5, 6], [7, 8]])
        self.matrix3 = Matrix([[6, 8], [10, 12]])
        self.matrix4 = Matrix([[19, 22], [43, 50]])
        self.matrix5 = Matrix([[1, 2], [3, 4]])
        self.matrix6 = Matrix([[1, 2, 3], [4, 5, 6]])
        self.matrix7 = Matrix([[1, 2], [3, 5]])

    def test_addition(self):
        result = self.matrix1 + self.matrix2
        self.assertEqual(result, self.matrix3)

    def test_multiplication(self):
        result = self.matrix1 * self.matrix2
        self.assertEqual(result, self.matrix4)

    def test_addition_invalid_size(self):
        with self.assertRaises(ValueError):
            self.matrix5 + self.matrix6

    def test_multiplication_invalid_size(self):
        with self.assertRaises(ValueError):
            self.matrix1 * self.matrix7

if __name__ == '__main__':
    unittest.main(verbosity=0)