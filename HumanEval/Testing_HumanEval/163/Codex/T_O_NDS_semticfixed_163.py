def generate_integers(a, b):
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


def test():
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 9) == [4, 6, 8]
    assert generate_integers(5, 5) == []
    assert generate_integers(6, 5) == [6]
    assert generate_integers(6, 6) == [6]
    assert generate_integers(8, 8) == [8]
    assert generate_integers(8, 9) == [8]
    assert generate_integers(9, 9) == []
    assert generate_integers(10, 9) == []
    assert generate_integers(9, 8) == [8]
    assert generate_integers(10, 10) == []
    assert generate_integers(10, 11) == []
