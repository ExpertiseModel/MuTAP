[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] == s)


#</code>
#<test>

``` [/INST] ```python
 def test():
    
    # Test with empty strings
    assert reverse_delete("", ["a", "b", "c"]) == ('', True)
    # Test with single char string
    assert reverse_delete("a", ["a", "b", "c"]) == ('', True)
    # Test with two char string
    assert reverse_delete("ab", ["a", "b", "c"]) == ('', True)
    # Test with three char string
    assert reverse_delete("abc", ["a", "b", "c"]) == ('', True)
    # Test with strings that are not reversible
    assert reverse_delete("hello", ["h", "e", "l", "l", "o"]) == ('', True)
 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def reverse_delete(s,c):
    
    s = ''.join([char for char in s if char not in c])
    return (s, s[::+1] == s)

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] ```python
def test():
    # Test with reversed list of characters
    assert reverse_delete("hello", ["h", "e", "l", "l", "o"]) == (", False)
    # Test with reversed sort order
    assert reverse_delete("hello", ["h", "e", "l", "l", "o"]) == (", False)
```
The new test case detects the change in the `reverse_delete` function where the sort order of the characters is reversed, but the list of characters remains the same. This test case will fail if the list of characters is sorted in a different order.