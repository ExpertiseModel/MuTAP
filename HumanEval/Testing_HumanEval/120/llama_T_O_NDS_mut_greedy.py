def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans
assert maximum([1, 2, 3], 2) == [2, 3]
