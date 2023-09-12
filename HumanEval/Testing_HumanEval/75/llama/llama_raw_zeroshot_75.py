[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def is_multiply_prime(a):
    
    def is_prime(n):
        for j in range(2,n):
            if n%j == 0:
                return False
        return True




    for i in range(2,101):
        if not is_prime(i): continue
        for j in range(2,101):
            if not is_prime(j): continue
            for k in range(2,101):
                if not is_prime(k): continue
                if i*j*k == a: return True
    return False


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `is_multiply_prime` function:
Test 1:
```python
a = 2
assert is_multiply_prime(a) == True
```
Test 2:
```python
a = 4
assert is_multiply_prime(a) == False
```
Test 3:
```python
a = 6
assert is_multiply_prime(a) == True
```
Test 4:
```python
a = 8
assert is_multiply_prime(a) == False
```
Test 5:
```python
a = 10
assert is_multiply_prime(a) == False
```
Test 6:
```python
a = 12
assert is_multiply_prime(a) == False
```
Test 7:
```python
a = 14
assert is_multiply_prime(a) == False
```
Test 8:
```python
a = 15
assert is_multiply_prime(a) == True
```
Test 9:
```python