from validate import *

def find_zero(f, interval, step):
    a = interval[0]
    b = interval[1]
    valid_interval(interval)
    found = False
    for i in range(int((b-a)/step)):
        x = i*step + a
        if f(x)*f(x+step) < 0:
            print(f"found interval: ({x} ; {x+step}) | f({x}) = {f(x)}, f({x+step}) = {f(x+step)}")
            found = True
    if not found:
        print("found no zeros")