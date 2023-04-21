import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
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


METADATA = {}



 # generate test case for the function above

def generate_test_case():
    assert find_zero([1, 0, -1]) == 1
    assert find_zero([1, 0, -4]) == 2
    assert find_zero([1, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, -8]) == 2
    assert find_zero([1, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, -16]) == 2
    assert find_zero([1, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, -32]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, -64]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, -128]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, -256]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, -512]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 1