import numpy as np


# create matrix
def create_matrix(i):
    while True:
        try:
            nrow = input("please input the row number of matrix" + i + ":")
            ncol = input("please input the column number of matrix" + i + ":")
            nrow = int(nrow)
            ncol = int(ncol)
            if nrow <= 0 or ncol <= 0:
                raise Exception()
            break
        except:
            print("Row number and Column number should be postive integers.")
            continue

    while True:
        try:
            matrix = input("Please input the integral elements of matrix" + i + ". Seperate with comma.")
            matrix = matrix.split(",")
            matrix = [int(x) for x in matrix]
            # print(matrix)
            if len(matrix) != nrow * ncol:
                raise Exception()
            break
        except:
            print("Please seperate with comma. Please input integers. Please input the right amount of elements.")
            continue

    nrow = int(nrow)
    ncol = int(ncol)

    mtx = np.array(matrix).reshape(nrow, ncol)
    print(mtx)
    return mtx


# matrix multiplication
def matrix_multiplication(mtx_1, mtx_2):
    if mtx_1.shape[1] != mtx_2.shape[0]:
        print(
            'wrong structure! Please make sure the column number of the first matrix is the same as the row number of the second matrix.')
    else:
        result = np.zeros((mtx_1.shape[0], mtx_2.shape[1]))
        for i in range(len(mtx_1)):
            for j in range(len(mtx_2[1])):
                for k in range(len(mtx_2)):
                    result[i][j] += mtx_1[i][k] * mtx_2[k][j]
    print("The multiplication matrix is:")
    return result


# create matrix_1
mtx_1 = create_matrix("1")

# create matrix_2
mtx_2 = create_matrix("2")

result = matrix_multiplication(mtx_1, mtx_2)
print(result)