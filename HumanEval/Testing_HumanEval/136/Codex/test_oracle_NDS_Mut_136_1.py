def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)



def test():
    assert largest_smallest_integers([1, -2, 3, -4, 5]) == (-2, 1)
    assert largest_smallest_integers([-1, 2, -3, 4, -5]) == (-1, 2)
    assert largest_smallest_integers([1, 2, -3, 4, -5]) == (1, 2)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-5, -1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (0, 0)
    assert largest_smallest_integers([-3, -2, -1, 0, 1, 3, -4]) == (-1, 0)
    assert largest_smallest_