def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0





def test():
    assert truncate_number(0.5) == 0.5
    assert truncate_number(1.4) == 0.4
    assert truncate_number(-0.5) == -0.5
    assert truncate_number(-1.4) == -0.4
    assert truncate_number(3.5) == 0.5
    assert truncate_number(1.5) == 0.5
    assert truncate_number(3.4) == 0.4
    assert truncate_number(4.5) == 0.5
    assert truncate_number(5.5) == 0.5

# print(test())

# test()

def test_cases():
    cases = [
        [
            1.1,
            0.1,
        ],
        [
            -1.1,
           