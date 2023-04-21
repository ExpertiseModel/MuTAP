def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

 # generate test case for the function above
def test_count_nums():
    assert count_nums([1, 2, 3]) == 3
    assert count_nums([1, -2, 3]) == 2
    assert count_nums([-1, -2, -3]) == 0
    assert count_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 11
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 13
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 14
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
    assert count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == 17
