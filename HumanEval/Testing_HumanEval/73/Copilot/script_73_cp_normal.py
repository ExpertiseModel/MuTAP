def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

 # generate test case for the function above

def test_smallest_change():
    assert smallest_change([1, 2, 3, 4, 5]) == 2
    assert smallest_change([1, 2, 3, 4, 5, 6]) == 3
    assert smallest_change([1, 1, 3, 3, 5, 5]) == 2
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7]) == 4
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9]) == 5
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11]) == 6
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13]) == 7
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15]) == 8
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17]) == 9
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19]) == 10
    assert smallest_change([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 11, 11, 13, 13, 15, 15, 17, 17, 19, 19, 21, 21]) == 11