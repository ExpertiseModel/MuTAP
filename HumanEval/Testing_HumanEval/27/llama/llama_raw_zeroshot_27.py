[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def flip_case(string: str) -> str:
    
    return string.swapcase()




# test case
def test():
    assert [/INST]  Certainly! Here are some test cases for the `flip_case` function:
```
def test_flip_case_empty_string():
    assert flip_case("") == ""

def test_flip_case_lowercase_string():
    assert flip_case("hello") == "HELLO"

def test_flip_case_mixed_case_string():
    assert flip_case("HeLlO") == "hello"

def test_flip_case_correct_case():
    assert flip_case("UpPerCASE") == "uppercase"

def test_flip_case_wrong_case():
    with pytest.raises(ValueError):
    flip_case("WrOnGcAsE")
```
Explanation:

* `test_flip_case_empty_string()`: Tests that the function returns an empty string for an empty input string.
* `test_flip_case_lowercase_string()`: Tests that the function returns the lowercase version of a lowercase input string.