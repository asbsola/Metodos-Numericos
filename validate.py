def belongs(x, I):
    valid_interval(I)
    if x > I[1] or x < I[0]:
        print("value does not belong to interval")
        return

def valid_interval(interval):
    if interval[0] > interval[1]:
        print("invalid interval format")
        return
    
def valid_bolzano(f, interval):
    if f(interval[0])*f(interval[1]) >= 0:
        print("bolzano doesnt apply")
        return