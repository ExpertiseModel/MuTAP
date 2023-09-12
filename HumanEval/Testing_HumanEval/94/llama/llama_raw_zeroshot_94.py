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
    assert [/INST]  Here are some test cases for the `skjkasdkd` function:
```
test_data = [
    # Test with a small list
    [2, 3, 5, 7, 11],
    # Test with a large list
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    # Test with a list of odd numbers
    [2, 3, 5, 7, 11, 13, 17, 19],
    # Test with a list of even numbers
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    # Test with a list of prime numbers
    [2, 3, 5, 7, 11, 13, 17, 19],
    # Test with a list of composite numbers
    [2, 4, 6, 8, 10, 12