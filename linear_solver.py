
# A matrix M is a 2-dimensional array (an array of arrays which represent rows)

def square_matrix(A):
    n = len(A)
    for i in range(n):
        if len(A[i]) != n:
            print("Matrix is not square")
            return

def upper_triangular(M):
    for i in range(len(M)):
        for j in range(i):
            if M[i][j] != 0:
                print("Matrix is not in upper triangular form")
                return

def backwards_substitution(A, b): # Ax = b where A is in upper triangular square matrix
    square_matrix(A)
    upper_triangular(A)
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j]*x[j]
        if A[i][i] == 0:
            print("Matrix is singular")
            return
        x[i] /= A[i][i]
    return x

def gaussian_elimination(A, b): # Ax = b where A is a square matrix
    square_matrix(A)
    n = len(A)
    for i in range(n-1):
        for k in range(i+1, n):
            coef = A[k][i]/A[i][i]
            A[k] = [A[k][j] - A[i][j]*coef for j in range(n)]
            b[k] -= b[i]*coef
    return backwards_substitution(A, b)

def jacobi(A, b, x_0, iterations): # Convergence requires A to be diagonally dominant (sum(|Aij|, j:{1..n}-{i}) < |Aii| for all i)
    square_matrix(A)
    n = len(A)
    x = [x_i for x_i in x_0]
    for k in range(iterations):
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if j != i:
                    x[i] -= x_0[j]*A[i][j]
            if A[i][i] == 0:
                print("Matrix is not diagonally dominant")
                return
            x[i] /= A[i][i]
        x_0 = [x_i for x_i in x]
    return x

def gauss_seidel(A, b, x_0, iterations): # Convergence requires A to be diagonally dominant (sum(|Aij|, j:{1..n}-{i}) < |Aii| for all i)
    square_matrix(A)
    n = len(A)
    x = x_0
    for k in range(iterations):
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if j != i:
                    x[i] -= x[j]*A[i][j]
            if A[i][i] == 0:
                print("Matrix is not diagonally dominant")
                return
            x[i] /= A[i][i]
    return x