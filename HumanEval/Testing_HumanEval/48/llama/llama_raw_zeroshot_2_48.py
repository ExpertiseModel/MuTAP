[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_palindrome(text: str):
    
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_palindrome` function using Python:
```
def test_is_palindrome():
    # Test with a simple palindrome
    assert is_palindrome("hello")

def test_is_not_palindrome():
    # Test with a non-palindrome
    assert not is_palindrome("not a palindrome")

def test_empty_string():
    # Test with an empty string
    assert not is_palindrome("")

def test_long_string():
    # Test with a long string
    assert is_palindrome("a very long string that is a palindrome")

def test_mixed_case():
    # Test with a mix of upper and lowercase letters
    assert is_palindrome("MIXeD_CaSe")

def test_with_num():
    # Test with a number in the string
    assert not is_palindrome("12345")

def test_with_symbol():
    # Test with a symbol in the string
    assert