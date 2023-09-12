[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_palindrome(string: str) -> bool:
    
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_palindrome` and `make_palindrome` functions:
---
### Tests for `is_palindrome` function

1. Test with a valid palindrome:
```python
assert is_palindrome("racecar")
```
2. Test with an invalid palindrome:
```python
assert not is_palindrome("hello")
```
3. Test with a string that is not a string:
```python
assert not is_palindrome(42)
```
4. Test with a string that is too long:
```python
assert not is_palindrome("a" * 100)
```
### Tests for `make_palindrome` function

1. Test with an empty string:
```python
assert make_palindrome("") == ""
```
2. Test with a valid palindrome:
```python
assert make_palindrome("racecar") == "racecarracecar"
```
3. Test with a string that is not a palindrome:
```python
assert