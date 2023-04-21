def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    """
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

 # generate test case for the function above

def test_unique_digits():
    assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
    assert unique_digits([11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == [11, 33, 55, 77, 99]
    assert unique_digits([111, 222, 333, 444, 555, 666, 777, 888, 999, 1000]) == [111, 333, 555, 777, 999]
    assert unique_digits([1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 10000]) == [1111, 3333, 5555, 7777, 9999]
    assert unique_digits([11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999, 100000]) == [11111, 33333, 55555, 77777, 99999]
