
def delta_poly(i, X, x):
    p = 1
    for x_k in X:
        if x_k != X[i]:
            p *= (x - x_k) / (X[i] - x_k)
    return p

def lagrange_poly(X, Y, x):
    L = 0
    for i in range(len(Y)):
        L += Y[i] * delta_poly(i, X, x)
    return L

def lagrange_error(K, X, x): # |D^(n+1)f| < K, x_0 < x < x_n
    e = K
    for i in range(len(X)):
        e *= (x-X[i])/(i+1)
    return abs(e) 

def newton_coeff(X, Y):
    M = []
    M.append(Y)
    n = len(Y)
    for i in range(n-1):
        last = M[i]
        next = []
        for k in range(n-i-1):
            next.append((last[k+1] - last[k]) / (X[k+i+1] - X[k]))
        M.append(next)
    return [M[i][0] for i in range(n)]

def print_newton_poly(X, Y):
    coef = newton_coeff(X, Y)
    for i in range(len(coef)):
        if coef[i] == 0:
            continue
        if coef[i] >= 0 and i > 0:
            print("+", end="")
        print(f"{coef[i]}", end="")
        if i > 0:
            print("*", end="")
        for j in range(i):
            if X[j] > 0:
                print(f"(x-{X[j]})", end="")
            elif X[j] < 0:
                print(f"(x+{-X[j]})", end="")
            else:
                print("x", end="")
    print("")

def newton_poly(X, Y, x):
    coeff = newton_coeff(X, Y)
    n = len(coeff)-1
    q = coeff[n]
    for i in range(n):
        q = coeff[n-i-1] + q*(x-X[n-i-1])
    return q

def combinatorial(n, i):
    p = 1
    for k in range(i+1, n+1):
        p *= k
    for k in range(n-i+1):
        p *= k

def bernstein(i, n, t):
    return combinatorial(n, i)*pow(t, i)*pow(t, n-i)

def bezier(C):
    a = 0
    n = len(C)
    for i in range(n):
        a += bernstein(i, n-1) * C[i]