def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))


#</code>
#<test>

def test():
    assert rounded_avg(3, 2) == -1
    assert rounded_avg(5, 3) == -1
    assert rounded_avg(7, 4) == -1
    assert rounded_avg(10, 5) == -1
    assert rounded_avg(12, 6) == -1
    assert rounded_avg(15, 7) == -1
    assert rounded_avg(18, 8) == -1
    assert rounded_avg(20, 9) == -1
