import matplotlib.pyplot as plt
from errors import *
from tabulate import tabulate

def derivative(f, x, h):
    return (f(x+h) - f(x))/h

def derivative_2(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)
