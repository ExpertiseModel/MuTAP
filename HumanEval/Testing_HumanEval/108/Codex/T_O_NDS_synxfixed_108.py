def count_nums(arr):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

def test():
    assert count_nums(-12) == 3
    assert count_nums(0) == 0
    assert count_nums(12) == 10
    assert count_nums(123) == 6
    assert count_nums(120) == 2
    assert count_nums(1234) == 4
    assert count_nums(12345) == 5
    assert count_nums(123450) == 3
    assert count_nums(123456789) == 9
    assert count_nums(12345678901234) == 1


test()
