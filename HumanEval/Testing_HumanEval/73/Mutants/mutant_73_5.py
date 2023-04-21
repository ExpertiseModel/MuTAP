def smallest_change(arr):
    
    ans = 0
    for i in range(len(arr) // 2):
       if not (arr[i] != arr[(len(arr) - i) - 1]):
            ans += 1
    return ans
