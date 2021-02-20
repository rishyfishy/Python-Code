def Thomas(matrix, vector):
    for i in range(len(vector)-1):
        factor = matrix[i][i]
        matrix[i][i] = 1
        matrix[i][i+1] /= factor
        vector[i] /= factor

        matrix[i+1][i+1] -= matrix[i][i+1]
        vector[i] -= vector[i]

    i = len(vector)-1
    factor = matrix[i][i]
    matrix[i][i] = 1
    matrix[i][i+1] /= factor
    vector[i] /= factor
    return matrix, vector