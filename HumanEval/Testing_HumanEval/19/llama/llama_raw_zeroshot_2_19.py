[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def sort_numbers(numbers: str) -> str:
    
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))




# test case
def test():
    assert [/INST]  Great! I'd be happy to help you generate test cases for the `sort_numbers` function. Here are a few test cases you can use to test the function:
```
# testcase 1: empty input
numbers = ""
assert sort_numbers(numbers) == ""

# testcase 2: invalid input
numbers = "zero one two three four five six seven eight nine"
assert sort_numbers(numbers) == ""

# testcase 3: valid input with duplicate values
numbers = "zero one two three three four five six seven eight nine"
assert sort_numbers(numbers) == "zero one two three four five six seven eight"

# testcase 4: valid input with numbers out of order
numbers = "nine eight seven six five four three two one zero"
assert sort_numbers(numbers) == "one two three four five six seven eight nine"

# testcase 5: valid input with large numbers
numbers = "nine eight seven six five four three two one zero one two three four five six seven eight nine"
assert sort_numbers(numbers) == "one two three four five six seven eight nine"
