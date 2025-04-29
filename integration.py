from validate import *
from math import sqrt

def left_area(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/n
    x = lambda i: I[0] + i*h
    return sum([h*f(x(i)) for i in range(n)])
    
def right_area(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/n
    x = lambda i: I[0] + i*h
    return sum([h*f(x(i)+h) for i in range(n)])

def midpoint_area(f, I, n = 1):
    valid_interval(I)
    h = (I[1]-I[0])/n
    x = lambda i: I[0] + i*h
    return sum([h*f(x(i)+h/2) for i in range(n)])

def trapez(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/n
    x = lambda i: I[0] + i*h
    return sum([(f(x(i)) + f(x(i+1))) * h / 2 for i in range(n)])

def trapez_error(f_prime, I, x):
    belongs(x, I)
    return f_prime(x)*pow(I[1] - I[0], 3)/12

def simpson_thirds(f, I, n=1):
    valid_interval(I)
    h = (I[1] - I[0])/(2*n)
    x = lambda i: I[0] + h*i
    return sum([(f(x(2*i)) + 4*f(x(2*i+1)) + f(x(2*i+2)))*h/3 for i in range(n)])

def simpson_third_error(f_forth, I, x):
    belongs(x, I)
    return pow((I[1]-I[0])/2, 5)*f_forth(x)/90

def simpson_three_eights(f, I):
    valid_interval(I)
    d = I[1] - I[0]
    h = d/3
    f_0 = f(I[0])
    f_1 = f(I[0]+h)
    f_2 = f(I[0]+2*h)
    f_3 = f(I[1])
    return h*(f_0 + 3*f_1 + 3*f_2 + f_3)*3/8

def simpson_three_eights_error(f_forth, I, x):
    belongs(x, I)
    return pow((I[1]-I[0])/3, 5)*f_forth(x)*3/80

def non_equidistant_two_points(f, I):
    valid_interval(I)
    a = I[0]
    b = I[1]
    x = lambda t: t*(b-a)/2 + (b+a)/2
    F = lambda t: f(x(t))*(b-a)/2
    return F(-1/sqrt(3)) + F(1/sqrt(3))

def non_equidistant_three_points(f, I):
    valid_interval(I)
    a = I[0]
    b = I[1]
    x = lambda t: t*(b-a)/2 + (b+a)/2
    F = lambda t: f(x(t))*(b-a)/2
    return 5/9*F(-sqrt(3)/sqrt(5)) + 8/9*F(0) + 5/9*F(sqrt(3)/sqrt(5))