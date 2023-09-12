[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair




# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `find_closest_elements` function:
```python
def test_find_closest_elements_empty_list():
    numbers = []
    result = find_closest_elements(numbers)
    assert result == ()

def test_find_closest_elements_single_element_list():

    numbers = [1.0]

    result = find_closest_elements(numbers)
    assert result == (1.0, 1.0)

def test_find_closest_elements_pair_of_equal_elements():
    numbers = [1.0, 1.0, 1.0]

    result = find_closest_elements(numbers)
    assert result == (1.0, 1.0)

def test_find_closest_elements_pair_of_unequal_elements():
    numbers = [1.0, 2.0, 3.0]

    result = find_closest_elements(numbers)
    assert result == (1.0, 2.0)