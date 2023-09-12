[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
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
    assert [/INST]  Certainly! Here are some test cases for the `sum_product` function in Python:
```
# Test 1: Basic input
numbers = [1, 2, 3]
assert sum_product(numbers) == (6, 2)

# Test 2: Input with duplicates
numbers = [1, 2, 2, 3]
assert sum_product(numbers) == (9, 6)

# Test 3: Negative input
numbers = [-1, -2, -3]
assert sum_product(numbers) == (-6, 2)

# Test 4: Zero input
numbers = [0, 0, 0]
assert sum_product(numbers) == (0, 1)

# Test 5: Large input
numbers = [1000, 1001, 1002]
assert sum_product(numbers) == (3003003, 3003003)
```
Explanation:
* Test 1: The function takes a list of integers `numbers`, and returns a tuple