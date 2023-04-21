def max_element(l: list):
    """Return maximum element in the list.
    """
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m


METADATA = {}



 # generate test case for the function above

def test_max_element():
    assert max_element([1]) == 1
    assert max_element([1, 2]) == 2
    assert max_element([2, 1]) == 2
    assert max_element([1, 2, 3]) == 3
    assert max_element([1, 3, 2]) == 3
    assert max_element([2, 1, 3]) == 3
    assert max_element([2, 3, 1]) == 3
    assert max_element([3, 1, 2]) == 3
    assert max_element([3, 2, 1]) == 3
    assert max_element([1, 2, 2]) == 2
    assert max_element([2, 1, 2]) == 2
    assert max_element([2, 2, 1]) == 2
    assert max_element([2, 2, 2]) == 2
    assert max_element([1, 1, 1]) == 1