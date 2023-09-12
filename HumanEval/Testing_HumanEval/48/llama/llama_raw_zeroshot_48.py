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
    assert [/INST]  Sure! Here are some test cases for the `is_palindrome` function:
```
# Test 1: Valid palindrome
def test_valid_palindrome():
    text = "racecar"
    assert is_palindrome(text) == True

# Test 2: Invalid palindrome
def test_invalid_palindrome():
    text = "hello"
    assert is_palindrome(text) == False

# Test 3: Edge cases
def test_edge_cases():
    text = ""
    assert is_palindrome(text) == False

# Test 4: Reverse case
def test_reverse_case():
    text = "racecar"
    assert is_palindrome(text.lower()) == True

# Test 5: Multiple words
def test_multiple_words():
    text = "foobar"
    assert is_palindrome(text) == False
```
These test cases cover different scenarios such as valid palindromes, invalid palindromes, edge cases, reverse case, and multiple words. You can run these tests