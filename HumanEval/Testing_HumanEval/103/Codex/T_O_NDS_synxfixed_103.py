def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

def test():
    assert rounded_avg(3, 12) == 6
    assert rounded_avg(0, 0) == 0
    assert rounded_avg(1, 1) == 0
    assert rounded_avg(2, 2) == 0
    assert rounded_avg(3, 12) == 6
    assert rounded_avg(7, 12) == 7


if __name__ == "__main__":
    test()
