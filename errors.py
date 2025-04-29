def abs_err(x, x_bar):
    return abs(x - x_bar)

def rel_err(x, x_bar):
    return abs_err(x, x_bar) / x

def find_iterations(err_form, max_search, expected_err):
    for i in range(max_search):
        e = err_form(i)
        if e < expected_err:
            print(f"enough iterations: {i}, err: {e}")
            return i