def median(l: list):
    
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0




# test case
def test():
    # Test with an empty list
    assert median([]) == None

    # Test with a list that contains only one element
    assert median([1]) == 1

    # Test with a list that contains multiple elements
    assert median([1, 2, 3, 4, 5]) == 3


    # Test with a list that is increasing
    assert median([1, 2, 3, 4, 5]) == 3

    # Test with a list that is decreasing
    assert median([5, 4, 3, 2, 1]) == 3
