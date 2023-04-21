def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    """
    return [n + 2*i for i in range(n)]

 # generate test case for the function above

def test_make_a_pile():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    assert make_a_pile(15) == [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]
    assert make_a_pile(20) == [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]
