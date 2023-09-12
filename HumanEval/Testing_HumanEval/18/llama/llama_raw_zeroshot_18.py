[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def how_many_times(string: str, substring: str) -> int:
    
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `how_many_times` function:

## Test 1: Positive case
def test_how_many_times_positive():
    string = "hello world"
    substring = "world"
    result = how_many_times(string, substring)
    assert result == 2

## Test 2: Negative case
def test_how_many_times_negative():
    string = "hello"
    substring = "lions"
    result = how_many_times(string, substring)
    assert result == 0

## Test 3: Edge case
def test_how_many_times_edge():
    string = "hello world ABC"
    substring = "world"
    result = how_many_times(string, substring)
    assert result == 3

## Test 4: Edge case
def test_how_many_times_edge():
    string = "hello world ABC"
    substring = "ABC"
    result = how_many_times(string, substring)
    assert result == 2

## Test