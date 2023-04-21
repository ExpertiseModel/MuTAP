def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

 # generate test case for the function above
def test_sort_array():
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 7]
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 12, 11, 13, 14, 15, 7]
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 12, 11, 13, 14, 15, 16, 7]
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 12, 11, 13, 14, 15, 16, 17, 7]
    assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 12, 11, 13, 14, 15, 16, 17, 18, 7]