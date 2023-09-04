from matrix import Matrix

def test_matrix_str():
    matrix = Matrix([[1, 2], [3, 4]])
    expected_output = "1 2\n3 4"
    assert str(matrix) == expected_output

def test_matrix_equal():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[1, 2], [3, 4]])
    matrix3 = Matrix([[5, 6], [7, 8]])

    assert matrix1 == matrix2
    assert not matrix1 == matrix3

def test_matrix_addition():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    expected_result = Matrix([[6, 8], [10, 12]])

    result = matrix1 + matrix2

    assert result == expected_result

def test_matrix_multiplication():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    expected_result = Matrix([[19, 22], [43, 50]])

    result = matrix1 * matrix2

    assert result == expected_result
