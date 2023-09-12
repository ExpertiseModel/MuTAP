[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `solution` function:
```py
def test():
    # Test with a simple list
    lst = [5, 8, 7, 1]
    assert solution(lst) == 12
    # Test with a list of only odd numbers
    lst = [3, 3, 3, 3, 3]
    assert solution(lst) == 9
    # Test with a list of only even numbers
    lst = [30, 13, 24, 321]
    assert solution(lst) == 0
    # Test with a list of mixed numbers
    lst = [3, 5, 7, 2, 1]
    assert solution(lst) == 11
    # Test with a list of negative numbers
    lst = [3, -5, 7, -2, 1]
    assert solution(lst) == 9
    # Test with a list of zero
    lst = [0, 1, 2, 3, 4]
    assert solution(lst) == 