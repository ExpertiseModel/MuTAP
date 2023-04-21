def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


METADATA = {}



 # generate test case for the function above

def test_monotonic():
    assert monotonic([1, 2, 3, 4, 5]) == True
    assert monotonic([5, 4, 3, 2, 1]) == True
    assert monotonic([1, 2, 3, 2, 1]) == False
    assert monotonic([1, 2, 3, 2, 1, 0]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]) == False
    assert monotonic([1, 2, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]) == False
