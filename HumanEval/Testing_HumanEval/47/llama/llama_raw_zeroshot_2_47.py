[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def median(l: list):
    
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `median` function:
```markdown
# Test cases for median() function
def test_empty_list():
    l = []
    assert median(l) is None

def test_single_element_list():
    l = [1]
    assert median(l) == 1

def test_list_with_ odd_number_of_elements():
    l = [1, 2, 3, 4, 5]
    assert median(l) == 3

def test_list_with_even_number_of_elements():
    l = [1, 2, 3, 4, 5, 6]
    assert median(l) == (3 + 3) / 2

def test_negative_values():
    l = [-1, -2, -3, -4, -5]
    assert median(l) == -3

def test_non_numeric_values():
    l = ['apple', 'banana', 'oranges']
    assert median(l) is None

def