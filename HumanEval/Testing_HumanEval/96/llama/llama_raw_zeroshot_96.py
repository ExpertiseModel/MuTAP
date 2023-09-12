[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def count_up_to(n):
    
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes



# test case
def test():
    assert [/INST]  Of course, here are some test cases for the `count_up_to()` function in Python:
```python
def test_count_up_to_primes_up_to_5():
    result = count_up_to(5)
    expected = [2, 3, 5]
    assert result == expected

def test_count_up_to_primes_up_to_10():
    result = count_up_to(10)
    expected = [2, 3, 5, 7, 11]
    assert result == expected

def test_count_up_to_non_primes():
    result = count_up_to(15)
    expected = []
    assert result == expected

def test_count_up_to_negative_number():
    with pytest.raises(ValueError):
    result = count_up_to(-5)
def test_count_up_to_zero():
    with pytest.raises(ValueError):
    result = count_up_to(0)
```
These test