def closest_integer(value):
    
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res



# test case

def test():
    # Test 1: Positive integer input
    assert closest_integer(5.5) == 6
    # Test 2: Negative integer input
    assert closest_integer(-5.5) == -6
    # Test 3: Non-decimal input
    assert closest_integer('apple') == 0
    # Test 4: Trailing zeros
    assert closest_integer(5.50) == 6
    # Test 5: Half-integer input
    assert closest_integer(5.5) == 6
    # Test 6: Non-integer input
    assert closest_integer('5.5abc') == 0
