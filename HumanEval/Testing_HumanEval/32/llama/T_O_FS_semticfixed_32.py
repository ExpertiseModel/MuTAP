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




#</code>
#<test>

def test():
    assert poly([1, 2, -3], 4) == -39.0
    assert poly([1, 2, -3], 2) == -7.0
    assert poly([1, 2, -3], -2) == -15.0
    assert poly([1, 2, 0], 3) == 7.0
    assert poly([1, 2, 0], -3) == -5.0
    assert poly([1, 0, -3], 4) == -47.0
    assert poly([0, 1, -3], 4) == -44.0
    assert poly([0, 1, 0], -3) == -3.0

    assert find_zero([1, -2, 3]) == 2.0    
    assert find_zero([1, 2, -3]) == -0.33333333337213844
    assert find_zero([1, 2]) == -0.5000000000582077
    assert find_zero([-6, 11, -6, 1]) == 0.9999999999417923
