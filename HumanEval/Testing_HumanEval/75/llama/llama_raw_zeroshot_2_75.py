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
1. Test the base case:
```
def test_base_case():
    assert is_multiply_prime(2) == True

test.test_base_case()
```
2. Test that the function returns False for composite numbers:
```
def test_composite():
    assert is_multiply_prime(5) == False

test.test_composite()
```
3. Test that the function returns True for a prime number multiplied by composites:
```
def test_ compose():
    assert is_multiply_prime(7) == False
    assert is_multiply_prime(7, 2) == True

test.test_compose()
```
4. Test that the function handles multiple arguments:
```
def test_ Multiple_args():
    assert is_multiply_prime(2, 3) == True

test.test_Multiple_args()
```
5. Test that the function handles large numbers:
```
def test_large_numbers():
    assert is_