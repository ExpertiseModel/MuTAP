[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def skjkasdkd(lst):
    
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result



# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `skjkasdkd` function using Python:
```
def test():
    # Test with a list of prime numbers
    lst = [2, 3, 5, 7, 11]
    result = skjkasdkd(lst)
    # Verify the result
    assert result == 21

# Test with a list of non-prime numbers
lst = [4, 6, 8, 9, 10]
result = skjkasdkd(lst)
# Verify the result
assert result == 0

# Test with a list of mixed prime and non-prime numbers
lst = [2, 3, 5, 7, 11, 4, 6, 8, 9, 10]
result = skjkasdkd(lst)
# Verify the result
assert result == 21

# Test with a very large list
lst = [x for x in range(1, 1000)]
result = skjkasdkd(lst)
# Verify the result