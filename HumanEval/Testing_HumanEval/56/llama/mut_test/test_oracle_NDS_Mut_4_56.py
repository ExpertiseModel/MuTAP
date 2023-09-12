[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 def correct_bracketing(brackets: str):
    
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0




# test case

``` [/INST] ```python
 def test():
    
    # Test 1: Valid brackets
    assert correct_bracketing("><ABC}</>def") == False

    # Test 2: Invalid brackets
    assert correct_bracketing("ABC</def") == False

    # Test 3: Depth exceeds limit
    assert correct_bracketing("><ABC</def") == False

    # Test 4: Depth is zero
    assert correct_bracketing(">ABC</def") == False

    # Test 5: Mix of valid and invalid brackets
    brackets = "><ABC</defXYZ</def"
    assert correct_bracketing("><ABC</defXYZ</def") == False

    # Test 6: Empty brackets
    assert correct_bracketing("") == True

    # Test 7: Brackets are nested
    assert correct_bracketing("><ABC</def>def") == False

    # Test 8: Brackets
 ```  [INST] #The test cases that you generated in test(), cannot detect the mutation in the following code snippet.
```python
def correct_bracketing(brackets: str):
    
    depth = 0
    for b in brackets:
        if b == "<":
            depth -= 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0



```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST]  I understand. Here's a new test case that can detect the mutation in the updated code snippet:
```python
def test():
    # Test 9: Brackets are swapped
    brackets = "><ABC</defXYZ</def"
    assert correct_bracketing("><ABC</defXYZ</def") == False


```
This test case will pass if the `correct_bracketing()` function returns `False` when given the modified input `">><ABC</defXYZ</def`.