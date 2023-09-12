def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m




def test():
    assert max_element([1, 2, 3]) == 3
    assert max_element([1, 2, 3, 4]) == 4
    assert max_element([1, 2, 3, 4, 5]) == 5

    assert max_element([]) is None

    assert max_element([1, 2, 3]) == 3

    assert max_element([3, 2, 4, 1, 5]) == 5

    assert max_element([3, 2, 4, 1, 5, 2]) == 5