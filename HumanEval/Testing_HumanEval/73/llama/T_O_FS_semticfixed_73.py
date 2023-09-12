def smallest_change(arr):
    
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans


#</code>
#<test>

def test():
    assert smallest_change([]) == 0

    assert smallest_change([5]) == 0

    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5

    
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5

#</test>

