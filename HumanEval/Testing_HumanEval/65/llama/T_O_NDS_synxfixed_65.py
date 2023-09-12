def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


# test case
def test():
    # Test 1: Positive shift
    assert circular_shift("Hello World!", 3) == "lllo wrld!"

    # Test 2: Negative shift
    assert circular_shift("Hello World!", -3) == "HwWrld!"

    # Test 3: Shift exceeds length of input string
    assert circular_shift("Hello World!", 5)

