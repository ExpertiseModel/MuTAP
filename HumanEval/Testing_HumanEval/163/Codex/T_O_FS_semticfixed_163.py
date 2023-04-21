def generate_integers(a, b):
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


def test():
    assert generate_integers(3, 5) == [4]
    assert generate_integers(5, 3) == [4]

