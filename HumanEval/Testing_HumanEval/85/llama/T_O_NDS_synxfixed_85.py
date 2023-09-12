
def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


# test case
def test():
    
    assert add([]) == []


    assert add([1]) == [1]


    assert add([1, 3, 5, 7, 9]) == [15, 17, 21, 23, 25]


    assert add([2, 4, 6, 8, 10]) == [16, 18, 20, 22, 24]

    assert add( [1, 3, 5, 7, 9, 2, [3, 5, 7, 9]]) == [2, 10, 15, 17, 21, 23, 25]
