def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

 # generate test case for the function above

def test_circular_shift():
    assert circular_shift(12345, 1) == "51234"
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift(12345, 3) == "34512"
    assert circular_shift(12345, 4) == "23451"
    assert circular_shift(12345, 5) == "12345"
    assert circular_shift(12345, 6) == "51234"
    assert circular_shift(12345, 7) == "45123"
    assert circular_shift(12345, 8) == "34512"
    assert circular_shift(12345, 9) == "23451"
    assert circular_shift(12345, 10) == "12345"
    assert circular_shift(12345, 11) == "51234"
    assert circular_shift(12345, 12) == "45123"