[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def fruit_distribution(s,n):
    
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `fruit_distribution` function:
```
# Test 1: Single digit input
s = '1 2 3 4 5'
n = 5
assert fruit_distribution(s, n) == 0

# Test 2: Multiple digits input
s = '12 34 56'
n = 3
assert fruit_distribution(s, n) == -3

# Test 3: Non-integer input
s = '1.5 2.2 3.3'
n = 2
assert fruit_distribution(s, n) == -1

# Test 4: Zero input
s = ' '
n = 0
assert fruit_distribution(s, n) == 0

# Test 5: Negative input
s = '-1 -2 -3'
n = -1
assert fruit_distribution(s, n) == -3

# Test 6: Empty input
s = ''
n = 5
assert fruit_distribution(s, n) == 0

# Test 7: