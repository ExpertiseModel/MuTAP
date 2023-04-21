def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


# test case
def test():
    assert maximum([1, 2, 3, 4, 5, 6, 7, 8], 0) == []
    assert maximum([1, 2, 3, 4, 5, 6, 7, 8], 1) == [8]
    assert maximum([1, 2, 3, 4, 5, 6, 7, 8], 2) == [7, 8]
    assert maximum([1, 2, 3, 4, 5, 6, 7, 8, 10], 3) == [6, 7, 8]
    assert maximum([1, 2, 3, 4, 5, 6, 7, 8, 10], 4) == [5, 6, 7, 8]
