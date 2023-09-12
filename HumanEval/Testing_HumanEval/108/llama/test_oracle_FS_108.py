
def count_nums(arr):
    
    def digits_sum(n):
        neg = 1
        if n < 0: 
            n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


#</original code>



#<test>
def test():
    
    assert count_nums([4, 2, 6, 8, 3, 1]) == 4
    assert count_nums([4, 2, 6, 8, -1, 3, 1]) == 3
    assert count_nums([4, 2, 6, 8, -1, -1, 3, 1]) == 2
    assert count_nums([4, 2, 6, 8, -1, -1, -1, 3, 1]) == 1
    assert count_nums([4, 2, -6, 8, -1, -1, -1, -1, 3]) == 0