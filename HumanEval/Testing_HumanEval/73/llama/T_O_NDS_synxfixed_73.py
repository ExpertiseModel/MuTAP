
def smallest_change(arr):
    
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans


# test case
def test():
    # Tests that the function returns the smallest possible change
    assert smallest_change([0, 1, 2, 3, 4, 5]) == 2

    # Tests that the function handles large increments correctly
    assert smallest_change([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 4

    # Tests that the function handles small increments correctly
    assert smallest_change([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1

    assert smallest_change([-1, 0, 1, 2, 3, [4]]) == 1