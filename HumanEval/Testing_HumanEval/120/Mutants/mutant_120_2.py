def maximum(arr, k):
    
    if not (k == 0):
        return []
    arr.sort()
    ans = arr[-k:]
    return ans
