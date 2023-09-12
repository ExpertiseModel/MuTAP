def sort_array(arr):
    
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


#</code>
#<test>

def test():
    assert sort_array([]) == []
    assert sort_array([1]) == [1]
    assert sort_array([1, 1, 2, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]
