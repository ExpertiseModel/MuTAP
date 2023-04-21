def smallest_change(arr):
    
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

def test():
    assert smallest_change([1, 4, 0, 4, 1, 3, 3, 0, 1, 1, 4, 0, 3, 3, 4, 1, 3, 3, 4, 0, 1, 4, 1, 3]) == 2
    assert smallest_change([1, 3, 1, 3, 0, 3, 3, 0, 1, 1, 3, 0, 1, 1]) == 1
    assert smallest_change([1, 2, 0, 2, 1, 2, 3, 2, 0, 2, 1, 2, 3, 1, 3, 4, 3, 0, 1, 2, 1, 2]) == 9
