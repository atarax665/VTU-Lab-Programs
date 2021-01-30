# To compute product of two matrices by 2D Array manipulation

# accept user input to create 2D matrix
def input_matrix():
    row, column = [int(x) for x in input("Enter rows and columns of Matrix: ").split()]
    matrix = []
    print("Enter the elements of this matrix:")
    for i in range(0, row):
        temp = []
        for j in range(0, column):
            temp.append(int(input()))
        matrix.append(temp)
    return matrix


# Print 2D matrix with correct format
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
    return


if __name__ == "__main__":
    matrix1 = []
    matrix2 = []
    prduct_matrix = []
    # input two matrics
    matrix1 = input_matrix()
    print("Matrix 1 are: ")
    print_matrix(matrix1)
    
    matrix2 = input_matrix()
    print("Matrix 2 are: ")
    print_matrix(matrix2)

    if len(matrix1[0]) != len(matrix2):
        print("Matrices are incompatible!, try again.")
        exit(0)

    # product matrix rows and cols
    rows, cols = (len(matrix1), len(matrix2[0]))

    # init product matrix value
    prduct_matrix = [[0 for x in range(cols)] for y in range(rows)]

    # iterate through rows of first matrix
    for i in range(rows):
        # iterate through columns of second matrix
        for j in range(cols):
            # iterate through rows of second matrix
            for k in range(len(matrix2)):
                prduct_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Product of matrices are: ")
    print_matrix(prduct_matrix)

    """ 
    Sample output
    
    Matrix 1 are:
    12 7 3
    4 5 6
    7 8 9
    Matrix 2 are:
    5 8 1 2
    6 7 3 0
    4 5 9 1

    Product of matrices are:
    114 160 60 27
    74 97 73 14
    119 157 112 23
    """