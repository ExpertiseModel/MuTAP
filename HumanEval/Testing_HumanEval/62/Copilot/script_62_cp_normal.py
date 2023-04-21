def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    """
    return [(i * x) for i, x in enumerate(xs)][1:]


METADATA = {}



 # generate test case for the function above

def test_derivative():
    assert derivative([1, 2, 3, 4, 5]) == [2, 6, 12, 20]
    assert derivative([1, 2, 3, 4, 5, 6]) == [2, 6, 12, 20, 30]
    assert derivative([1, 2, 3, 4, 5, 6, 7]) == [2, 6, 12, 20, 30, 42]
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 6, 12, 20, 30, 42, 56]
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 6, 12, 20, 30, 42, 56, 72]
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 6, 12, 20, 30, 42, 56, 72, 90]
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [2, 6, 12, 20, 30, 42, 56, 72, 90, 110]
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132]
    assert derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [2, 6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156]