def generate_integers(a, b):
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


#</code>
#<test>

def test():
    assert generate_integers(0, 0) == []

    assert generate_integers(2, 2) == [2]


    assert generate_integers(8, 8) == [8]


    assert generate_integers(3, 5) == [4]

    assert generate_integers(4, 6) == [4, 6]


    assert generate_integers(1, 3) == [2]
