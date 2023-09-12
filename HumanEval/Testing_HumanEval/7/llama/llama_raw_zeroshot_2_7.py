[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `filter_by_substring` function:
```
def test_filter_by_substring_empty_list():
    substring = "hello"
    assert filter_by_substring([], substring) == []

def test_filter_by_substring_single_string():
    substring = "hello"
    strings = ["hello", "world", "hello"]
    assert filter_by_substring(strings, subgroup) == ["hello"]

def test_filter_by_substring_multiple_substrings():
    substring = "hello"
    strings = ["hello", "world", "hello", "hello", "world"]
    assert filter_by_substring(strings, subgroup) == ["hello", "hello"]

def test_filter_by_substring_unicode():
    substring = u"😊"
    strings = ["hello", "world", "hello", "😊"]
    assert filter_by_substring(strings, subgroup) == ["hello", "😊"]

def test_filter_by_substring_list_of_lists():
   