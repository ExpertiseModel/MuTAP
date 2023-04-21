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




def test():
    assert find_zero([1, 3, -2, -5, 6]) == 0.618033989, "Should be {0}".format(0.618033989)    
    assert find_zero([1, 3, -2, -5, 6]) == 1.618033989, "Should be {0}".format(1.618033989)    
    assert find_zero([-0.04, -1.44, 1.58, 3.52, 6.22, -1.62]) == -0.027022484922781587
