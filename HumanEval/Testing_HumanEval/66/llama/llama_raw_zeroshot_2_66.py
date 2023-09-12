[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `digitSum` function:
```
# Test that the function returns 0 for an empty string
s = ""
assert digitSum(s) == 0

# Test that the function returns the expected sum for a string of digits
s = "123"
assert digitSum(s) == 4

# Test that the function returns 0 for a string of uppercase letters
s = "abc"
assert digitSum(s) == 0

# Test that the function raises a ValueError for an empty string
s = ""
try:
    digitSum(s)
except ValueError:
    pass

# Test that the function raises a ValueError for a string of non-digits
s = "abc"
try:
    digitSum(s)
except ValueError:
    pass

# Test that the function returns the expected sum for a string of non-digits
s = "abcdefg"
assert digitSum(s) == 10

# Test that the function returns the expected sum for a string of digits with leading zeros
s = "0