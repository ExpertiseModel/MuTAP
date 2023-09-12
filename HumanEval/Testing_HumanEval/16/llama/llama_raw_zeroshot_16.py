[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `count_distinct_characters` function in Python:
```
def test_valid_strings():
    # Valid strings should return a correct count of distinct characters
    assert count_distinct_characters("hello") == 3
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("hello world") == 5

def test_empty_string():
    # The function should return 0 for an empty string
    assert count_distinct_characters("") == 0

def test_special_chars():
    # Special characters should be handled correctly
    assert count_distinct_characters("\u0000") == 1
    assert count_distinct_characters("\u00ff") == 1

def test_mixed_case():
    # Lowercase and uppercase strings should be handled correctly
    assert count_distinct_characters("HeLlo") == 3
    assert count_distinct_characters("hello") == 3

def test_unicode():