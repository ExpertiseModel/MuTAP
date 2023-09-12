
def generate_integers(a, b):
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


# test case

def test():
    # Test with different inputs
    assert generate_integers(1, 2) == [2]
    assert generate_integers(3, 4) == [4]
    assert generate_integers(4, 6) == [4, 6]
    assert generate_integers(2, 3) == [2]
    # Test edge cases
    assert generate_integers(0, 1) == []
    assert generate_integers(1, 0) == []
    assert generate_integers(10, 11) == []
    # Test range of numbers
    assert generate_integers(10, 20) == []
