def gaussSeidel(matrix, vector, error):  # n=3
    # Assume matrix is diagonally dominant, or that gauss seidel will converge.

    x1_old = 0
    x2_old = 0
    x3_old = 0

    e1 = 1000
    e2 = 1000
    e3 = 1000

    while (e1 & e2 & e3 < error):
        x1 = matrix[1, 1] = (vector[1]-x2_old*matrix[1, 2] -
                             x3_old*matrix[1, 3])/matrix[1, 1]
        e1 = (x1_old - x1)/x1
        x1_old = x1
        x2 = matrix[2, 2] = (vector[2]-x1_old*matrix[2, 1] -
                             x3_old*matrix[2, 3])/matrix[2, 2]
        e2 = (x2_old - x2)/x2
        x2_old = x2
        x3 = matrix[3, 3] = (vector[3]-x1_old*matrix[3, 1] -
                             x2_old*matrix[3, 2])/matrix[3, 3]
        e3 = (x3_old - x3)/x3
        x3_old = x3
    return  x1, x2, x3
