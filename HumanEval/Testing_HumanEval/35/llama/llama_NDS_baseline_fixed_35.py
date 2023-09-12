def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m




# test case

def test():
    assert max_element([1, 2, 3, 4, 5]) == 5
    assert max_element([1, 2, 3, 4, 5, 5]) == 5
    assert max_element([1, 2, 2, 3, 3, 3]) == 3
    assert max_element([1, 2, 2, 3, 3, 3]) == 3
