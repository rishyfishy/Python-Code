
def naiveGaussJordan(matrix: list, vector: list):
    n = len(matrix)
    # Forward Propogation
    for k in range(n-1):

        for i in range(k+1, n):
            factor = matrix[i][k]/matrix[k][k]

            for j in range(k+1, n):
                
                matrix[i][j] -= factor*matrix[k][j]

            vector[i] -= factor*vector[k]
            print(matrix)
    # Back-substitution
    x = n*[0]
    x[n-1] = vector[n-1]/matrix[n-1][n-1]

    for i in reversed(range(1, n)):
        sum = vector[i]
        for j in range(i+1, n):
            sum -= matrix[i][j]*x[j]
        x[i] = sum/matrix[i][j]

    return x

# %%
def partialPivoting(matrix:list,vector:list)->list:
    n=len(vector)
    x=n*[0]

 


    for k in range(1, n):
    # Swap the first row and the row with max first element

       #zero out first column
        for i in range(k+1, n+1):
            factor = matrix[i, k]/matrix[k, k]

            for j in range(k+1, n+1):
                matrix[i, j] -= factor*matrix[k, j]

            vector[i] -= factor*vector[k]

a=[[1,2,3],[1,4,9],[1,8,27]]
b=[0,0,-6]
answer = naiveGaussJordan(a,b)
print(answer)

# %%
