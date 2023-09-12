[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)


# test case
def test():
    assert [/INST]  Of course! Here are some test cases for the `sorted_list_sum` function:
```python
def test_empty_list():
    lst = []
    assert sorted_list_sum(lst) == []

def test_single_word_list():
    lst = ["aa"]
    assert sorted_list_sum(lst) == ["aa"]

def test_duplicate_words():
    lst = ["aa", "aa", "bb"]
    assert sorted_list_sum(lst) == ["aa", "bb"]

def test_length_order():
    lst = ["aa", "cd", "ab", "a", "bb"]
    assert sorted_list_sum(lst) == ["a", "ab", "bb", "cd"]

def test_alphabetical_order():
    lst = ["aa", "ab", "a", "bb", "cd"]
    assert sorted_list_sum(lst) == ["a", "ab", "bb", "cd"]

def test_odd_length_words():
    lst = ["aa", "a", "cd", "b"]