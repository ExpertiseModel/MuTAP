[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


# test case

``` [/INST] ```python
 def test():
    
    assert is_bored("I am bored.") ==  1

    assert is_bored("I am really bored.") == 1

    assert is_bored("I am so bored.") == 1

    assert is_bored("I am wondering if I am bored.") == 1

    assert is_bored("I am so bored!!") == 1
 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum((sentence[:2] == 'I ' for sentence in sentences))

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] To detect the change in the code snippet, we can modify the existing test cases to check if the function is case-sensitive. Here's a new test case that will catch the change:
```python
# test case
def test():
    assert is_bored("i am bored.") == 0
    assert is_bored("i AM Bored.") == 1
    assert is_bored("i Am Bored.") == 1
    assert is_bored("i Bored.") == 1
    assert is_bored("i BORED.") == 1
 ```
In this new test case, we are checking if the function returns `0` when the sentence is not in uppercase. The existing test cases only check if the first two characters are 'I ' and do not consider case sensitivity. By adding this new test case, we can ensure that the function works correctly even if the sentence is in uppercase.