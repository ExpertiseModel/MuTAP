def generate_integers(a, b):
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


#</code>
#<test>
def test():
  
    assert generate_integers(0, 0) == []

    assert generate_integers(2, 2) == [2, 4]


    assert generate_integers(8, 8) == [0, 2, 4, 6, 8]


    assert generate_integers(3, 5) == [3, 5, 7, 9]

    assert generate_integers(4, 6) == [4, 6, 8, 10]


    assert generate_integers(1, 3) == [1, 3]