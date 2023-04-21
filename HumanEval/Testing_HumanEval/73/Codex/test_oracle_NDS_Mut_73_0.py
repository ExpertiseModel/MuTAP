def smallest_change(arr):
    
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans



def test():
    assert len([1, 1, 1, 0, 1, 1, 0, 1, 1]) == 4
    assert smallest_change([1, 1, 1, 0, 1, 1, 0, 1, 1]) == 4

