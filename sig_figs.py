from errors import *

def sig_figs(x , x_bar):
    k = 1
    figs = 0
    while(rel_err(x, x_bar) < 10**(-k)/2):
        figs = k
        k = k + 1
    return figs

print(sig_figs(1.12, 1.123))