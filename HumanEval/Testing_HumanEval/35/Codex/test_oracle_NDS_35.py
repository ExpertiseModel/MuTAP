def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m



def test():
    assert max_element([5]) == 5
    assert max_element([1,2,3]) == 3
    assert max_element([3,2,1]) == 3
    assert max_element([3,3,3]) == 3
    assert max_element([1,1,1,1]) == 1
    assert max_element([1,2,2,2,2]) == 2
    assert max_element([1,1,1,1,1]) == 1
    assert max_element([1,2,1,1,1,1]) == 1
    assert max_element([2,2,2,2,2,2,2]) == 2
    print("Passed.")


test()
