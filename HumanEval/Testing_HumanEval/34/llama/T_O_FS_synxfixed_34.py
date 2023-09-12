def unique(l: list):
    
    return sorted(list(set(l)))

def test():
 
    assert unique([1, 2, 2, 3, 3, 4]) == [1, 2, 2, 3, 3, 4]
    assert unique([1, 2, 3, 3, 4, 4]) == [1, 2, 3, 4]
    assert unique([1, 2, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique([]) == []
    assert unique([1]) == [1]


