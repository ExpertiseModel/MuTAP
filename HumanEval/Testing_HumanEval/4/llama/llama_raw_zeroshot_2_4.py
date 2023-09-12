[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `mean_absolute_deviation` function:
```
test_cases = [
    # Simple list of numbers
    ({4, 6, 8, 10}, 5.0),
    # List with numerical values
    ({9.5, 10.5, 11.5, 12.5}, 7.5),
    # List with non-numerical values
    (["apple", 3.14, "orange", 0.5], 4.0),
    # List with negative values
    ([-4.0, -6.0, -8.0, -10.0], -7.0),
    # List with empty value
    ([] , 0.0),
    # List with null value
    (null, np.nan),
    # List with large numbers
    (range(10), 5.0),
    # List with float values
    ({0.1, 0.2, 0.3, 0.4, 0.5}, 0.3