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


#</code>
#<test>
def test():
    
    assert minSubArraySum([-1, 2, -3, 4, -1, 2]) == -9
    assert minSubArraySum([1, 2, 3, 4, 5]) == 0
    assert minSubArraySum([-1, -2, -3, -4, -5]) == -10
    assert minSubArraySum([1, 2, 3, 4, 5, 6]) == 0
    assert minSubArraySum([-2, -1, -3, -4, -5, -6]) == -12
    assert minSubArraySum([1, 2, 3, 4, 5, 6, 7]) == 0