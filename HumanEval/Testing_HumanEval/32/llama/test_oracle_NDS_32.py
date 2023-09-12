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




# test case
def test():
    # Test the poly function
    assert poly([1, 2], 3) == 6.0
    assert poly([-1, 2], 3) == -6.0
    assert poly([1, -2], 3) == 2.0
    assert poly([-1, 1], 3) == 0.0

    # Test the find_zero function
    assert find_zero([1, 2, 3]) == 1.5
    assert find_zero([-1, -2, 3]) == -1.5
    assert find_zero([1, 2, -3]) == 2.5
    assert find_zero([-1, 2, -3]) == -2.5

    # Test the find_zero function with multiple inputs
    assert find_zero([1, 2], [3, 4]) == 2.5
    assert find_zero([-1, -2], [3, 4]) == -3.5
