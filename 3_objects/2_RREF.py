from matrices import *

matrix1 = Matrix([[1,2,3],[4,5,6], [7,8,0]])

def exists_pivot_row(matrix, column_number):
    column = Matrix([[matrix.matrix[i][column_number]] for i in range(matrix.num_rows())])
    
    print(column)

exists_pivot_row(matrix1,1)