def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))


# test case

def test():
    # Test with positive numbers
    assert rounded_avg(5, 10) == "0b1000"
    assert rounded_avg(10, 15) == "0b1100"
    assert rounded_avg(20, 25) == "0b10110"

    # Test with negative numbers
    assert rounded_avg(-5, 10) == "0b10"
    assert rounded_avg(-10, 15) == "0b10"
    assert rounded_avg(-20, 25) == "0b10"

    # Test edge cases
    assert rounded_avg(0, 1) == "0b0"
    assert rounded_avg(0, 0) == "0b0"
    assert rounded_avg(1, 0) == "-1"
