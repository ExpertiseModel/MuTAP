def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


def test():
    assert largest_smallest_integers([1, 2, -3, 4, 5]) == (-3, 1)
    assert largest_smallest_integers([1, -2, 3, 4, -5]) == (-2, 1)
    assert largest_smallest_integers([1, 2, 3, -4, 5]) == (-4, 1)
