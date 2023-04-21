def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    """
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if (s < 0):
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sum

 # generate test case for the function above
def test_minSubArraySum():
    assert minSubArraySum([1, -2, 3, -2]) == -3
    assert minSubArraySum([5, -3, 5]) == -3
    assert minSubArraySum([3, -1, 2, -1]) == -1
    assert minSubArraySum([3, -2, 2, -3]) == -3
    assert minSubArraySum([-2, -3, -1]) == -6