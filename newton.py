epsilon = 10**-20

# f must be C2(interval) and f'(x) != 0 at root for convergence
# if f' and f'' of constant sign then the convergence is monotonous when f(x_0)*f''(x_0) > 0
def newton(f, f_prime, X_0, iterations, err_bound):
    x_0 = X_0
    E = 0
    iter = 0
    for i in range(1, iterations+1):
        if abs(f_prime(x_0)) < epsilon:
            print(f"f' too close to 0 at iteration {i}")
            return
        iter = i
        E = abs(f(x_0)/f_prime(x_0))
        x_0 = x_0 - f(x_0)/f_prime(x_0)
        if(E < err_bound):
            break
    print(f"iterations: {i}, root: {x_0}, step-diff: {E}")
    