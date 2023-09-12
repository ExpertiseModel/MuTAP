from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value




# test case

def test():
    # Test 1: Basic input
    assert sum_product([1, 2, 3]) == (6, 6)

    # Test 2: Input with duplicates
    assert sum_product([1, 2, 2, 3]) == (8, 12)

    # Test 3: Negative input
    assert sum_product([-1, -2, -3]) == (-6, -6)

    # Test 4: Zero input
    assert sum_product([0, 0, 0]) == (0, 0)

    # Test 5: Large input
    assert sum_product([1000, 1001, 1002]) == (3003, 1003002000)

