[INST] <<SYS>>
#You are a python coding assistant. Always answer with python code.
<</SYS>>

#Generate test cases for the following function:```python
 def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)


#</code>
#<test>

``` [/INST] ```python
 def test():
    
    assert order_by_points([ -3, -2, -1, 0, 1, 2, 3 ]) == [-3, -2, -1, 0, 1, 2, 3]


    assert order_by_points([ 3, 2, 1, 0, 1, 2, 3 ]) == [0, 1, 1, 2, 2, 3, 3]


    assert order_by_points([ -3, 2, -1, 0, 1, 2, 3 ]) == [-3, -1, 0, 1, 2, 2, 3]


    assert order_by_points([]) ==[]
 ```  [INST] #The test cases that you generated in test() function, cannot detect the change in the following code snippet.
```python
def order_by_points(nums):
    
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] / neg
        return sum(n)
    return sorted(nums, key=digits_sum)

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] I understand, you want me to generate a new test case that can detect the change in the `digits_sum` function in the modified code snippet. Here is an example of how you can modify the `test` function to detect this change:
```python
def test():
    # Test the original code
    result1 = order_by_points([-3, -2, -1, 0, 1, 2, 3])
    assert result1 == [-3, -2, -1, 0, 1, 2, 3]

    # Test the modified code
    result2 = order_by_points([-3, 2, -1, 0, 1, 2, 3])
    assert result2 == [-3, 2, -1, 0, 1, 2, 3]

    # Test the modified code with a different input
    result3 = order_by_points([3, 2, -1, 0, 1, 2, 3])
    assert result3 == [0, 1, 1, 2, 2, 