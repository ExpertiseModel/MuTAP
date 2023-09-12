[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def total_match(lst1, lst2):
   
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2


# test case
def test():
    assert [/INST]  Great, here are some test cases for the `total_match` function:
```
def test_empty_lists():
    lst1 = []
    lst2 = []
    assert total_match(lst1, lst2) is None

def test_unequal_lengths():
    lst1 = ["a", "b", "c"]
    lst2 = ["a", "b", "c", "d"]
    assert total_match(lst1, lst2) is None

def test_unequal_strings():
    lst1 = ["apple", "banana", "cherry"]
    lst2 = ["apple", "orange", "lemon"]
    assert total_match(lst1, lst2) is None

def test_same_strings():
    lst1 = ["apple", "banana", "cherry"]
    lst2 = ["apple", "banana", "cherry"]
    assert total_match(lst1, lst2) == lst1

def test_list_containment():
    lst1 = ["apple", "banana", "cherry"]
    lst2