def rounded_avg(n, m):
    
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))
assert rounded_avg(3, 12) == "0b1000"
assert rounded_avg(1, 1) == "0b1"
