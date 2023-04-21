import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin


assert find_zero([1.001, 2, 1, -3]) == 1.1579297038842924
assert find_zero([-1.5, 1.5, 0.5, -0.5]) == 0.9999999999417923
assert find_zero([1, 2]) == -0.5000000000582077
assert find_zero([]) == -1.0
