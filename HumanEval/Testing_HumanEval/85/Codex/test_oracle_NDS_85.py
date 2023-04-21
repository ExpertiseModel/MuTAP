def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def test():
    assert add([1, 2, 3, 4, 5, 6]) == 4
    assert add([1, 2, 3, 4, 5, 6, 5]) == 7
    assert add([1, 2, 3, 4, 5, 6, 5, 4]) == 7
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1]) == 7
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2]) == 7
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2, 3]) == 7
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2, 3, 4]) == 7
    assert add([1, 2, 3, 4, 5, 6, 5, 4, 1, 2,