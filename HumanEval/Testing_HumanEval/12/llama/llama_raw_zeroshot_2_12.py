[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `longest` function:
```python
def test_empty_list():
    # Test with empty list
    assert longest([]) is None

def test_single_string():
    # Test with a single string
    assert longest(["hello"]) == "hello"

def test_multi_strings():
    # Test with multiple strings
    assert longest(["hello", "world", "python"]) == "python"

def test_empty_strings():
    # Test with empty strings
    assert longest(["", " ", "  "]) == ""

def test_mixed_strings():
    # Test with a mix of empty and non-empty strings
    assert longest(["", "hello", "world", "", "python"]) == "python"

def test_longest_string():
    # Test with a very long string
    assert longest(["a" * 100]) == "a" * 100

def test_raise_valueError():
    # Test with invalid input
    with pytest.raises(ValueError):
    longest([