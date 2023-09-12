[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `maximum` function:
    ```
    # Test 1: Small arrays and k = 3
    arr = [1, 2, 3]
    k = 3
    assert maximum(arr, k) == [2, 2, 1]

    # Test 2: Large array and k = 2
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    assert maximum(arr, k) == [4, 5]

    # Test 3: Edge cases
    arr = [-10, -1, 2, 3]
    k = 1
    assert maximum(arr, k) == [-1, 2, 3]

    # Test 4: Negative k
    arr = [1, 2, 3]
    k = -1
    assert maximum(arr, k) == [-3, -2, -1]

    # Test 5: Multiple max values
    arr = [1, 2, 3,