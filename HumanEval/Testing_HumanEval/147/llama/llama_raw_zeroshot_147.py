[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def get_max_triples(n):
    
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `get_max_triples` function:
```python
# Test 1: Valid input
n = 1
assert get_max_triples(n) == 0

# Test 2: Small input
n = 3
assert get_max_triples(n) == 3

# Test 3: Large input
n = 100
assert get_max_triples(n) == 27

# Test 4: Edge case
n = 2
assert get_max_triples(n) == 1

# Test 5: Input not in the range of [1,n]
n = -1
assert get_max_triples(n) == 0

# Test 6: Input equal to n
n = 1
assert get_max_triples(n) == 0
```
Here is the code for each test case:

```python
def test():
    # Test 1: Valid input
    n = 1
    assert get_max_triples(n) == 0
