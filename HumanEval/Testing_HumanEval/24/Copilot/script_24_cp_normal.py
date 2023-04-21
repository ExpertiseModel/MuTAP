def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n % i == 0:
            return i


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above


def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(16) == 8
    assert largest_divisor(17) == 1
    assert largest_divisor(18) == 9