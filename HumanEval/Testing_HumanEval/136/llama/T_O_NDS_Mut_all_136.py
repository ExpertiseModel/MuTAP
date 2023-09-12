def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


# test case

def test():
    assert largest_smallest_integers([]) == (None, None)

    assert largest_smallest_integers([1]) == (None, 1)

    assert largest_smallest_integers([-1]) == (-1, None)

    assert largest_smallest_integers([1, -2, 3, -4]) == (-2, 1)

    assert largest_smallest_integers([1, 2, 3, 4]) == (None, 1)

    assert largest_smallest_integers([-1, -2, -3, -4]) != (None, None) # This line will fail if the mutation is present
    # Test the original function
    assert largest_smallest_integers([1, -2, 3, -4]) == (-2, 1)
    # Test the function with a different input
    assert largest_smallest_integers([1, 2, 3, 4]) == (None, 1)
    # Test the function with a negative input
    assert largest_smallest_integers(["a"]) == (None, None)

