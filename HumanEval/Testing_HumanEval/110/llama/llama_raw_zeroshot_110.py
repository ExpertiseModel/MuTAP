[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def exchange(lst1, lst2):
    
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            odd += 1
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"
            


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `exchange` function using Python:
```
def test():
    # Test with lists of different sizes
    assert exchange([1, 2, 3], [4, 5, 6]) == "YES"
    assert exchange([1, 2, 3], [4, 5, 6, 7]) == "NO"
    # Test with odd and even elements
    assert exchange([1, 2, 3], [4, 5, 6]) == "YES"
    assert exchange([1, 2, 3], [4, 5, 6, 7]) == "NO"
    # Test with lists of different types
    assert exchange([1, 2, 3], [True, False, True]) == "YES"
    assert exchange([1, 2, 3], [False, True, False]) == "NO"
    # Test with negative inputs
    assert exchange([1, 2, 3'], [ Nan, NaN, Nan]) == "YES"
    assert exchange([1, 2, 3'], [Nan,