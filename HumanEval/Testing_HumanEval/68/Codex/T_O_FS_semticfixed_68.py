def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]


def test():
    assert pluck(['a','b','c','b','d']) == ['b','c','d','b','d','b']    
    assert pluck([1,2,3,4,5]) == [2, 1]
    assert pluck([1,2,3,4,5,6]) == [2, 1]
   