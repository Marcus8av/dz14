class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in row]) for row in self.matrix])

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(
                other.matrix[0]):
            result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
        raise ValueError("Матрицы должны быть одинакового размера для сложения!")

    def __mul__(self, other):
        if isinstance(other, Matrix) and len(self.matrix[0]) == len(other.matrix):
            result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(other.matrix)):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(result)
        raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!")

    def print_info(self):
        print("Матрица:")
        print(self)

matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])

print(matrix1)  
print(matrix2)

print ("Cравнение матриц:")
print(matrix1 == matrix2)  

print ("Cложение матриц:")
matrix3 = matrix1 + matrix2  
matrix3.print_info()  

print ("Умножение матриц:")
matrix4 = matrix1 * matrix2  
matrix4.print_info()  