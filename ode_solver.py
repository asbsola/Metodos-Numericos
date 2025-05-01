from validate import *;
from errors import *;

def euler(interval, F, y_0, h):
    partitions = int((interval[1] - interval[0]) / h)
    y = [0] * (partitions+1)
    y[0] = y_0
    h = (interval[1] - interval[0]) / partitions
    for i in range(0, partitions):
        t = i * h + interval[0]
        y[i+1] = y[i] + F(t, y[i]) * h
    return y

def euler_second(interval, F, F_prime, y_0, h):
    partitions = int((interval[1] - interval[0]) / h)
    y = [0] * (partitions+1)
    y[0] = y_0
    h = (interval[1] - interval[0]) / partitions
    for i in range(0, partitions):
        t = i * h + interval[0]
        y[i+1] = y[i] + F(t, y[i]) * h + F_prime(t, y[i]) * h * h / 2
    return y

def runge_kutta_second_order(interval, F, y_0, h, coef):
    partitions = int((interval[1] - interval[0]) / h)
    (a, b, p, q) = coef
    y = [0] * (partitions+1)
    y[0] = y_0
    h = (interval[1] - interval[0]) / partitions
    for i in range(0, partitions):
        t = i * h + interval[0]
        k1 = F(t, y[i]) * h
        k2 = F(t + p*h, y[i] + q*k1) * h
        y[i+1] = y[i] + a*k1 + b*k2
    return y

def runge_kutta_forth_order(interval, F, y_0, h):
    partitions = int((interval[1] - interval[0]) / h)
    y = [0] * (partitions+1)
    y[0] = y_0
    h = (interval[1] - interval[0]) / partitions
    for i in range(partitions):
        t = i * h + interval[0]
        k1 = F(t, y[i]) * h
        k2 = F(t + h/2, y[i] + k1/2) * h
        k3 = F(t + h/2, y[i] + k2/2) * h
        k4 = F(t + h, y[i] + k3) * h
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6
    return y

def heun(interval, F, y_0, h):
    return runge_kutta_second_order(interval, F, y_0, h, (0.5, 0.5, 1, 1))

def euler_second_rugen_kutta(interval, F, y_0, h):
    return runge_kutta_second_order(interval, F, y_0, h, (0, 1, 0.5, 0.5))

def ralston(interval, F, y_0, h):
    return runge_kutta_second_order(interval, F, y_0, h, (1/3, 2/3, 3/4, 3/4))

def back_and_forth_err(interval, F, y_0, h):
    partitions = int((interval[1] - interval[0]) / h)
    y = euler(interval, F, y_0, partitions)
    neg_interval = [interval[1], interval[0]]
    z = euler(neg_interval, F, y[partitions], partitions)
    return abs_err(z[partitions], y_0)

def half_step_err(interval, F, y_0, h):
    partitions = int((interval[1] - interval[0]) / h)
    y1 = euler(interval, F, y_0, partitions)
    y2 = euler(interval, F, y_0, 2*partitions)
    return [abs_err(y1[i], y2[2*i]) for i in range(partitions + 1)]