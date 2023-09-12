[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `simplify` function:
```
test_cases = [
    ("1/5", "5/1"),  # Success
    ("1/6", "2/1"),  # Success
    ("7/10", "10/2"),  # Failure ( denominator is not a whole number )
    ("3/2", "2/1"),  # Success
    ("4/3", "3/1"),  # Success
    ("13/4", "4/1"),  # Failure ( numerator is not a whole number )
    ("0/1", "1/1"),  # Success
    ("-1/2", "-2/1"),  # Success
    ("-3/4", "-4/1"),  # Failure ( denominator is not a whole number )
]
def test():
    for x, n in test_cases:
        result = simplify(x, n)
        print(f"{x} * {n}: {result}")

test()
```
Explanation:

* The first and third