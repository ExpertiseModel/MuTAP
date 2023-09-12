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
   
    assert poly([1, 2, -3], 4) == 14.0
    assert poly([1, 2, -3], 2) == 7.0
    assert poly([1, 2, -3], -2) == -14.0
    assert poly([1, 2, 0], 3) == 12.0
    assert poly([1, 2, 0], -3) == -9.0
    assert poly([1, 0, -3], 4) == 0.0
    assert poly([0, 1, -3], 4) == 0.0
    assert poly([0, 1, 0], -3) == -3.0

    assert find_zero([1, -2, 3]) == 2.0
    assert find_zero([1, 2, -3]) == 1.5
    assert find_zero([1, 2]) == -0.5
    assert find_zero([-6, 11, -6, 1]) == 1.0