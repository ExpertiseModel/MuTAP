def maximum(arr, k):
    
    if k != 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans
