def Thomas(matrix, vector):
    '''
    Void function that solves tridiagonal systems of equations
    inputs:
        matrix: a square matrix describing the system _A_
        vector: the input vector _x_

    '''
    #forward prop
    for i in range(len(vector)-1):
        matrix[i][i+1] /= matrix[i][i]
        vector[i] /= matrix[i][i]
        matrix[i][i] = 1

        matrix[i+1][i+1] -= matrix[i+1][i]*matrix[i][i+1]
        vector[i+1]-=matrix[i+1][i]*vector[i]
        matrix[i+1][i]=0

    i=len(vector)-1
    vector[i] /= matrix[i][i]
    matrix[i][i] = 1

    #backprop

    for i in reversed(range(len(vector)-1)):
        vector[i]-=matrix[i][i+1]*vector[i+1]
        matrix[i][i+1]=0






# matrix=[[2,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,0],[0,0,-1,2,-1],[0,0,0,-1,2]]
# vector=[1,1,1,1,1]

# Thomas(matrix,vector)
# for i in matrix:
#     print (i)
# print('\n')
# print([round(x,5) for x in vector])