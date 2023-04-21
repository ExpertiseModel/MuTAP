from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value



 # generate test case for the function above

def test_sum_product():
    assert sum_product([1, 2, 3]) == (6, 6)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
    assert sum_product([1, 2, 3, 4, 5, 6]) == (21, 720)
    assert sum_product([1, 2, 3, 4, 5, 6, 7]) == (28, 5040)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8]) == (36, 40320)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (45, 362880)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (55, 3628800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == (66, 39916800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == (78, 479001600)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == (91, 6227020800)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == (105, 87178291200)
    