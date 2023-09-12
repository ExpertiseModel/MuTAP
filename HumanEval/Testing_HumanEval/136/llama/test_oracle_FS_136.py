def largest_smallest_integers(lst):
    
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


#</code>
#<test>
def test():
   

    assert largest_smallest_integers([]) == (None, None)


    assert largest_smallest_integers([3]) == (3, 3)


    assert largest_smallest_integers([2, 3]) == (3, 2)


    assert largest_smallest_integers([2, -3, 4, -5]) == (-5, 4)

    assert largest_smallest_integers([5, 3, 2, 4]) ==(5, 3)