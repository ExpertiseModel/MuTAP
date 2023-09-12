#<original code>



def derivative(xs: list):
    
    return [(i * x) for i, x in enumerate(xs)][1:]





#<test>

def test():
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([1, 2, 3, 4]) == [2, 6, 12]
    assert derivative([1, 2, 3, 4, 5]) == [2, 6, 12, 20]
    assert derivative([1, 2, 3, 4, 5, 6]) == [2, 6, 12, 20, 30]
    assert derivative([1, 2, 3, 4, 5, 6, 7]) == [2, 6, 12, 20, 30, 42]
