def maximum(arr, k):
    
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans
assert maximum([1, 2, 3, 4, 5, 6, 7, 8], 1) == [8]
