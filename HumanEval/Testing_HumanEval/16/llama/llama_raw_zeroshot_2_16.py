[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def count_distinct_characters(string: str) -> int:
    
    return len(set(string.lower()))




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `count_distinct_characters` function:
```
def test_empty_string():
    string = ""
    assert count_distinct_characters(string) == 0

def test_single_character_string():
    string = "a"
    assert count_distinct_characters(string) == 1

def test_mixed_case_string():
    string = "AbaBcDeFgHiJ"
    assert count_distinct_characters(string.lower()) == 5

def test_long_string():
    string = "The quick brown fox jumped over the lazy dog."
    assert count_distinct_characters(string) == 10

def test_string_with_digits():
    string = "Hello123World!"
    assert count_distinct_characters(string) == 6

def test_string_with_punctuation():
    string = "Hello World! How are you today?")
    assert count_distinct_characters(string) ==