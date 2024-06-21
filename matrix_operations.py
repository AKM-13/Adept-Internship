import unittest

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def dimensions(self):
        return len(self.matrix), len(self.matrix[0])

    def add(self, other):
        if self.dimensions() != other.dimensions():
            raise ValueError("Matrices must be of the same size.")
        
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        
        return Matrix(result)

    def subtract(self, other):
        if self.dimensions() != other.dimensions():
            raise ValueError("Matrices must be of the same size.")
        
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        
        return Matrix(result)

    def multiply(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                sum = 0
                for k in range(len(other.matrix)):
                    sum += self.matrix[i][k] * other.matrix[k][j]
                row.append(sum)
            result.append(row)
        
        return Matrix(result)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
# Unit tests for Matrix class
if __name__ == "__main__":
    # Test matrices
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    # Test addition
    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)
    print("Addition:")
    print(matrix1.add(matrix2))

    # Test subtraction
    print("Subtraction:")
    print(matrix1.subtract(matrix2))

    # Test multiplication
    matrix3 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix4 = Matrix([[7, 8], [9, 10], [11, 12]])
    print("Matrix 3:")
    print(matrix3)
    print("Matrix 4:")
    print(matrix4)
    print("Multiplication:")
    print(matrix3.multiply(matrix4))
