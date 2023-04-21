def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    """
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

 # generate test case for the function above
def test_rounded_avg():
    assert rounded_avg(1, 10) == '0b1011'
    assert rounded_avg(1, 100) == '0b1100101'
    assert rounded_avg(1, 1000) == '0b1001001001'
    assert rounded_avg(1, 10000) == '0b1000100010001'
    assert rounded_avg(1, 100000) == '0b1000010000100001'
