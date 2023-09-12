def derivative(xs: list):
    
    return [(i * x) for i, x in enumerate(xs)][1:]




# test case

def test():
    # Test with a list of numbers
    assert derivative([1, 2, 3, 4, 5]) == [2, 6, 12, 20]
    # Test with a list of strings
    assert derivative(['a', 'b', 'c', 'd', 'e']) == ['b', 'cc', 'ddd', 'eeee']
    #
