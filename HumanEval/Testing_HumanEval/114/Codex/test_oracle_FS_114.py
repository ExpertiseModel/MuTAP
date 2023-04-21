def minSubArraySum(nums):
    
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

def test():
    assert minSubArraySum([1, 2, 3, 4, 5]) == 1
    assert minSubArraySum([1, 2, 3, 4, 5, -10]) == -10
    assert minSubArraySum([1, 2, 3, 4, 5, -1]) == -1
    assert minSubArraySum([]) == 0
