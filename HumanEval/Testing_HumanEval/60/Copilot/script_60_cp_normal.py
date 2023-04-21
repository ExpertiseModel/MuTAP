def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    """
    return sum(range(n + 1))


METADATA = {}



 # generate test case for the function above

def test_sum_to_n():
    assert sum_to_n(1) == 1
    assert sum_to_n(2) == 3
    assert sum_to_n(3) == 6
    assert sum_to_n(4) == 10
    assert sum_to_n(5) == 15
    assert sum_to_n(6) == 21
    assert sum_to_n(7) == 28
    assert sum_to_n(8) == 36
    assert sum_to_n(9) == 45
    assert sum_to_n(10) == 55
    assert sum_to_n(11) == 66
    assert sum_to_n(12) == 78
    assert sum_to_n(13) == 91
    assert sum_to_n(14) == 105
    assert sum_to_n(15) == 120
    