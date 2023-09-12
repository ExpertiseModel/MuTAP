def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


# test case
def test():
    # Test with valid input
    assert fruit_distribution("apple banana orange", 5) == 5
    assert fruit_distribution("apple banana orange", 6) == 1
    # Test with invalid input
    assert fruit_distribution("apple banana orange", 5) == 5
    assert fruit_distribution("apple banana orange", 6) == 0
    # Test with empty string
    assert fruit_distribution("", 5) == 0
    assert fruit_distribution("", 6) == 0
    # Test with null input
    assert fruit_distribution( None, 5) == 0
    assert fruit_distribution( None, 6) == 0