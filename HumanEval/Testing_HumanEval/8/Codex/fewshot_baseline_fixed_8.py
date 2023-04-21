from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value




def test():
    assert sum_product([1, 2, 3, 4]) == (10, 24)
    assert sum_product([1, 2, 3, 4, 5]) == (15, 120)
