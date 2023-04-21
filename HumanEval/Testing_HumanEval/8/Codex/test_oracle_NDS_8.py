from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value



def test():
    assert sum_product([1, 2, 3]) == (6, 6)
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
    assert sum_product([1, 2, 3, 4, 5, 6]) == (21, 720)
    assert sum_product([1, 2, 3, 4, 5, 6, 7]) == (28, 5040)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8]) == (36, 40320)
    assert sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (45, 362880)
    assert sum_product([1, 2, 3, 4, 5, 6, 7,