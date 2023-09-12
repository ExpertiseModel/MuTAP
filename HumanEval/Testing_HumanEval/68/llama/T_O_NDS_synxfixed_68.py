def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]


# test case
def test():
  
    assert pluck([]) == []

    assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9]) == []

    assert pluck([2, 4, 6, 8, 10]) == [2]

    assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18]) == [4, 6, 8, 10]
