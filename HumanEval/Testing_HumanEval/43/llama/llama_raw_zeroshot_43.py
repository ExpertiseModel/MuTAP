[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def pairs_sum_to_zero(l):
    
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False




# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `pairs_sum_to_zero` function:
```
# Test that the function returns True for a pair of numbers that sum to 0
def test_pairs_sum_to_zero_true():
    l = [1, 2, 3, 4, 5]
    assert pairs_sum_to_zero(l) == True

# Test that the function returns False for a non-existent pair of numbers that sum to 0
def test_pairs_sum_to_zero_false():
    l = [1, 2, 3, 4, 5]
    assert pairs_sum_to_zero([6, 7, 8, 9, 10]) == False

# Test that the function works for a list of negative numbers
def test_pairs_sum_to_zero_negatives():
    l = [-1, -2, -3, -4, -5]
    assert pairs_sum_to_zero(l) == True

# Test that the function works for a list of positive and negative