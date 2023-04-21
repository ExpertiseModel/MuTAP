def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)

def test():
    assert largest_smallest_integers([4, -4, 3, -2, -1]) == (4, -2)
    assert largest_smallest_integers([4, -4, 3, -2, -1, -200]) == (4, -200)
    assert largest_smallest_integers([4, -4, 3, -2, -1, 200]) == (4, 200)
    assert largest_smallest_integers([-1, -200, -3, -5]) == (-200, -5)
    assert largest_smallest_integers([1, 2, 3, -4, 5]) == (1, 5)
    assert largest_smallest_integers([1, -2, 3, -4, 5]) == (-2, 5)
    assert largest_smallest_integers([-1, 2,-3, 4, -5]) == (-1, -5)
    