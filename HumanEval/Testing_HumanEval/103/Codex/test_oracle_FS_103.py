def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

def test():
    assert rounded_avg(1, 10) == 3
    assert rounded_avg(1, 8) == 2.5
    assert rounded_avg(1, 7) == 2
    assert rounded_avg(1, 5) == 1.5
    assert rounded_avg(1, 3) == 1
