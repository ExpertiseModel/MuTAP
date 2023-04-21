def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    """
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]

 # generate test case for the function above

def test_pluck():
    assert pluck([1, 2, 3, 4, 5]) == [2, 1]
    assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert pluck([1, 1, 3, 3, 5, 5]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7, 9, 9]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19]) == []
    assert pluck([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21]) == []