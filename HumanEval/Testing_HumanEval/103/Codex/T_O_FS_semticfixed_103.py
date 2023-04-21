def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))


def test():
    assert rounded_avg(1, 10) == 0b110
    assert rounded_avg(1, 8) == 0b100
    assert rounded_avg(1, 7) == 0b100
    assert rounded_avg(1, 5) == 0b11
    assert rounded_avg(1, 3) == 0b10
