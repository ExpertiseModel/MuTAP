[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def simplify(x, n):
    
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `simplify` function:
```
# Test 1: Simple cases
def test_simplify_simple():
    x = "4/5"
    n = "3/4"
    result = simplify(x, n)
    assert result == True

# Test 2: Non-simple cases
def test_simplify_non_simple():
    x = "10/20"
    n = "2/3"
    result = simplify(x, n)
    assert result == False

# Test 3: Negative numbers
def test_simplify_neg():
    x = "-4/5"
    n = "-3/4"
    result = simplify(x, n)
    assert result == True

# Test 4: Irrational numbers
def test_simplify_irrational():
    x = "3.5/4"
    n = "2.5/3"
    result = simplify(x, n)
    assert result == False

# Test 5: Zero division
def