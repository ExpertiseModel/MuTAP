
def add(lst):
    
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])


# test case

def test():
    assert add([]) == 0


    assert add([1]) == 0


    assert add([1, 3, 5, 7, 9]) == 0


    assert add([2, 4, 6, 8, 10]) == 12

    assert add( [1, 3, 5, 7, 9, 2, [3, 5, 7, 9]]) == 2

