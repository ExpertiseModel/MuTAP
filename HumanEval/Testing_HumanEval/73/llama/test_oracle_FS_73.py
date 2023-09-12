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

    assert smallest_change([5]) == 1

    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3

    
    assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0

#</test>

def test_edge_case():
    arr = [1, 2, 3, 