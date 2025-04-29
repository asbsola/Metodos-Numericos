from validate import *

def bisection_err(interval, iterations):
    valid_interval(interval)
    d = interval[1] - interval[0]
    return d/2**(iterations+1)

def bisection(f, interval, iterations): # f must be continuous
    a = interval[0]
    b = interval[1]
    valid_interval(interval)
    valid_bolzano(f, interval)
    iter = 0
    for i in range(iterations+1):
        iter = i
        x = (a + b)/2
        if f(x) == 0:
            break
        if f(a)*f(x) < 0:
            b = x
        if f(b)*f(x) < 0:
            a = x
    print(f"iterations: {iter} root: {x}, err: {bisection_err(interval, iterations)}")