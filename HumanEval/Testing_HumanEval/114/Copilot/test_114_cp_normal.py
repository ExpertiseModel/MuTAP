from script_114_cp_few_shot import minSubArraySum
def test_minSubArraySum():
    assert minSubArraySum([1, -2, 3, -2]) == -3
    assert minSubArraySum([5, -3, 5]) == -3
    assert minSubArraySum([3, -1, 2, -1]) == -1
    assert minSubArraySum([3, -2, 2, -3]) == -3
    assert minSubArraySum([-2, -3, -1]) == -6