import doctest
from matrix import Matrix

def test_matrix_operations():
    """

    >>> matrix1 = Matrix([[1, 2], [3, 4]])
    >>> matrix2 = Matrix([[5, 6], [7, 8]])
    >>> matrix3 = matrix1 + matrix2
    >>> print(matrix3)
    6 8
    10 12
    
    >>> matrix4 = matrix1 * matrix2
    >>> print(matrix4)
    19 22
    43 50
    
    >>> matrix5 = Matrix([[1, 2], [3, 4]])
    >>> matrix6 = Matrix([[1, 2, 3], [4, 5, 6]])
    >>> matrix7 = matrix5 * matrix6
    Traceback (most recent call last):
        ...
    ValueError: Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!

    >>> matrix8 = Matrix([[1, 2], [3, 4]])
    >>> matrix9 = Matrix([[1, 2], [3, 5]])
    >>> matrix10 = matrix8 + matrix9
    Traceback (most recent call last):
        ...
    ValueError: Матрицы должны быть одинакового размера для сложения!
    """

if __name__ == "__main__":
    doctest.testmod()