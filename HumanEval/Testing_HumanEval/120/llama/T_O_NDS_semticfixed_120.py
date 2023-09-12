
def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


# test case

def test():
    assert maximum([], 3) == []

   
    assert maximum([1, 2, 3], 2) == [2, 3]

    assert  maximum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4) == [7, 8, 9, 10]
    
    assert maximum([1, 2, 3], -3) == []

