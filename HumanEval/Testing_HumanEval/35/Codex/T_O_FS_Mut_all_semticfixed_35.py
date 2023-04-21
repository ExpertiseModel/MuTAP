def max_element(l: list):
    
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m






def test():
    assert max_element([1,2,3]) == 3
    assert max_element([0,7,3.14,25.01]) == 25.01
    assert max_element([1,2,3]) == 3
    assert max_element([1,2,3]) == 3
    assert max_element([1,2,3]) == 3
    assert max_element([]) == None    
    assert max_element(None) == None    
    assert max_element([]) == None    
    assert max_element(None) == None