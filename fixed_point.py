from validate import *

def fixed_point_err(f, K, x_0, iterations): # |f'| < K on interval
    step_0 = abs(f(x_0) - x_0)
    if K >= 1 or K < 0:
        print("bound must be smaller than 1 and greater than or equal to 0")
        return
    return K**iterations * step_0 / (1-K)

def fixed_point(f, K, X_0, interval, iterations): # f: interval -> interval must be C1(interval) and |f'| < K < 1
    valid_interval(interval)
    x_0 = X_0
    if K >= 1 or K < 0:
        print("bound must be smaller than 1 and greater than or equal to 0")
        return
    for i in range(1, iterations+1):
        if x_0 < interval[0] or x_0 > interval[1]:
            print("not contained in domain")
            return
        x_0 = f(x_0)
    print(f"root: {x_0}, err: {fixed_point_err(f, K, X_0, iterations)}")