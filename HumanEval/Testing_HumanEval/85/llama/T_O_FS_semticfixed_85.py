def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


#</original code>



def test():
    assert add([]) == 0
    assert add([1, 2, 3, 4, 5, 6]) == 12
    assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 20
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20
    assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
