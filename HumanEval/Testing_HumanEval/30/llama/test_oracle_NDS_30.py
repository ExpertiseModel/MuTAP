def get_positive(l: list):
    
    return [e for e in l if e > 0]




# test case
def test():
    # Test with a list of integers
    assert get_positive([1, 2, 3, 4, 5]) == [2, 3, 4]
    # Test with a list of floats
    assert get_positive([1.5, 2.2, 3.3, 4.4, 5.5]) == [2.2, 3.3, 4.4]
    # Test with a list of strings
    assert get_positive(['hello', 'world', 'foo', 'bar']) == ['world', 'bar']
    # Test with a list of lists
    list_of_lists = [[1, 2], [3, 4