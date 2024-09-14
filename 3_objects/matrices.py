def dot_product(l1,l2):
    if len(l1) != len(l2):
        raise ValueError('Dimensions must match in order to perform dot product')
    prod = 0
    for i in range(len(l1)):
        prod += l1[i]* l2[i]
    return prod



class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __str__(self):
        if isinstance(self.matrix[0], list):  # 2D matrix
            return '\n'.join(['[' + ' '.join(map(str, row)) + ']' for row in self.matrix])
        else:  # 1D matrix
            return '[' + ' '.join(map(str, self.matrix)) + ']'
    
    def shape(self):
        if isinstance(self.matrix[0], list):
            return len(self.matrix), len(self.matrix[0])  # 2D matrix
        return len(self.matrix), 1  # 1D matrix (considered as having 1 column)
    
    def num_rows(self):
        return len(self.matrix)
    
    def num_cols(self):
        if isinstance(self.matrix[0], list):
            return len(self.matrix[0])
        return 1  # 1D matrix has 1 column
    
    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrix must have the same dimensions to add.")
        
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)
    
    def __sub__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Matrix must have the same dimensions to subtract.")
        
        result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)
    
    def transpose(self):
        result = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(result)
    
    def scalar_multiply(self, scalar):
        result = [[scalar * self.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)
    
    def matrix_multiply(self, other):
        other = other.transpose()
        result = [[dot_product(self.matrix[i], other.matrix[j]) for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)
    
    def multiply(self, other):  # la hizo chatgpt
        """Performs matrix multiplication (dot product) between two matrices."""
        if self.num_cols() != other.num_rows():
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
        
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.num_cols())) 
                   for j in range(other.num_cols())] for i in range(self.num_rows())]
        return Matrix(result)
    
    def recursive_determinant(self):
        if self.num_rows() != self.num_cols():
            raise ValueError('Only square matrices have a determinant')
        if self.num_rows()== 1:
            return(self.matrix[0][0])
        else:
            sum = 0
            for i in range(self.num_cols()):
                pivot = self.matrix[0][i] #siempre tomaremos pivots de la primera fila para simplificarnos la vida
                comatrix = Matrix([row[:i] + row[i+1:] for k, row in enumerate(self.matrix) if k != 0])
                if i % 2 == 1:
                    value = comatrix.recursive_determinant()*(-1)*pivot
                else:
                    value = comatrix.recursive_determinant()*pivot
                sum += value
            return(sum)


# Example usage:
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
'''
# Add two Matrix
addition_result = matrix1 + matrix2
print("Addition Result:")
print(addition_result)

# Subtract two Matrix
subtraction_result = matrix1 - matrix2
print("\nSubtraction Result:")
print(subtraction_result)

# Transpose of a matrix
transpose_result = matrix1.transpose()
print("\nTranspose Result:")
print(transpose_result)

# Scalar multiplication
scalar_multiply_result = matrix1.scalar_multiply(2)
print("\nScalar Multiplication Result:")
print(scalar_multiply_result)
print('Rows and Cols of Matrix 1')
print(matrix1.num_rows())
print(matrix1.num_cols())'''
if __name__ == "__main__":
    matrix3 = Matrix([[4,2],[1,5]])
    matrix4 = Matrix([[1,2,3],[4,5,6], [7,8,0]])
    #print(matrix3)
    #print("")
    print(matrix4)
    print("")
    #print(matrix3.matrix_multiply(matrix4))
    print(matrix4.recursive_determinant())

