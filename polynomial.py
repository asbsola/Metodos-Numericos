def polynomial(coeff, x):
    y = 0
    for i in range(0, len(coeff)):
        y = y*x + coeff[i]
    return y
print(polynomial([2, 0, 1, 7], 8))