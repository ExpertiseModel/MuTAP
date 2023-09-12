#<original code>



def derivative(xs: list):
    
    return [(i * x) for i, x in enumerate(xs)][1:]





#<test>
def test():
   
    assert derivative([1, 2, 3]) == [2, 4, 6]
    assert derivative([1, 2, 3, 4]) == [2, 4, 6, 8]
    assert derivative([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
    assert derivative([1, 2, 3, 4, 5, 6]) == [2, 4, 6, 8, 10, 12]
    assert derivative([1, 2, 3, 4, 5, 6, 7]) == [2, 4, 6, 8, 10, 12, 14]