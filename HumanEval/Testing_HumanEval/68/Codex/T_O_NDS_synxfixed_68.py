def pluck(arr):
    
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]

def test():
    assert pluck([3, 8, 10]) == []
    assert pluck([3, 8, 10, 16]) == [3, 0]
    assert pluck([1, 2, 7, 10, 15]) == [1, 2]


# assert pluck([]) == []

# print("All test cases passed")
