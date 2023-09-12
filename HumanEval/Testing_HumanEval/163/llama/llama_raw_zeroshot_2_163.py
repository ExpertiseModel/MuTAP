[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]


# test case
def test():
    assert [/INST]  Here are some test cases for the `generate_integers` function:
```
Test 1: Valid range of inputs
    a = 2
    b = 8
    expected = [2, 4, 6, 8]
    actual = generate_integers(a, b)
    assert actual == expected

Test 2: Outside range of inputs
    a = 10
    b = 14
    expected = []
    actual = generate_integers(a, b)
    assert actual == expected

Test 3: Negative input
    a = -1
    b = 1
    expected = []
    actual = generate_integers(a, b)
    assert actual == expected

Test 4: Non-integer inputs
    a = "hello"
    b = "world"
    expected = []
    actual = generate_integers(a, b)
    assert actual == expected

Test 5: Edge case test
    a = 2
    b = 2
    expected = [2]
    actual = generate_integers(a, b