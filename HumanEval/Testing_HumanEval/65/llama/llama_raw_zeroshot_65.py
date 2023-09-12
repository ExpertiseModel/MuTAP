[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def circular_shift(x, shift):
    
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `circular_shift` function using Python code:
---
# Test 1: Positive shift
def test_circular_shift_positive_shift():
    # Setup
    x = "Hello World!"
    shift = 3

    # Run
    result = circular_shift(x, shift)

    # Expected
    expected = "lllo wrld!"
    assert result == expected

# Test 2: Negative shift
def test_circular_shift_negative_shift():
    # Setup
    x = "Hello World!"
    shift = -3

    # Run
    result = circular_shift(x, shift)

    # Expected
    expected = "HwWrld!"
    assert result == expected

# Test 3: Shift exceeds length of input string
def test_circular_shift_shift_exceeds_length():
    # Setup
    x = "Hello World!"
    shift = 5

    # Run
    result = circular_shift(x, shift)

