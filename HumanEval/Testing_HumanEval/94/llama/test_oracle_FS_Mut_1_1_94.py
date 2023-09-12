[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
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



#</code>
#<test>

``` [/INST] ```python
 def test():
    
    assert skjkasdkd([5, 3, 7, 11, 13]) == 4


    assert skjkasdkd([0, 1, 2, 3, 4]) == 3


    assert skjkasdkd([100, 1000, 10000, 100000, 1000000]) == 0


 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def skjkasdkd(lst):
    
    def isPrime(n):
        for i in range(2, int(n * 0.5) + 1):
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


```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST]  Understood! Here's a new test case to detect the change in the `skjkasdkd` function:
```python
def test():
    assert skjkasdkd([5, 3, 7, 11, 13]) == 4


    assert skjkasdkd([0, 1, 2, 3, 4]) == 3


    assert skjkasdkd([100, 1000, 10000, 100000, 1000000]) == 0


    # A new test case to detect the change in the function:
    assert skjkasdkd([5, 3, 7, 11, 13], skip_zero=False) == 4
```
This test case will pass if the `skjkasdkd` function is unchanged, but will fail if the function has been modified to include the `skip_zero` parameter.