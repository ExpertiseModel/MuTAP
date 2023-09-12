[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Fix the syntax error in the following code:
```python
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result




# test case
def test():
    #test_single_ element_list
    assert rolling_max([1]) == [1]

    #test_empty_list
    assert rolling_max([]) == []

    #test_list_of_ints
    assert rolling_max([1, 2, 3, 4, 5]) == [4, 5]

    #test_list_of_floats
    assert rolling_max([1.0, 2.0, 3.0, 4.0, 5.0]) == [4.0, 5.0]

    #test_list_of_negatives():
    assert rolling_max([-1, -2, -3, -4, -5]) == [-4, [/INST]  The syntax error in the code is the missing `=` after the `running_max` variable in the `for` loop. Here is the corrected code:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result



# test case
def test():
    #test_single_element_list
    assert rolling_max([1]) == [1]

    #test_empty_list
    assert rolling_max([]) == []

    #test_list_of_ints
    assert rolling_max([1, 2, 3, 4, 5]) == [4, 5]

    #test_list_of_floats
    assert rolling_max([1.0, 2.0, 3.0, 4.0