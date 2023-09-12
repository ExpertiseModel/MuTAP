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
        n[0] = n[0] // neg
        return sum(n)
    return sorted(nums, key=digits_sum)

```
#Generate a new test case to detect this change.
```python
# test case
def test():
    assert [/INST] Ah, I see. In that case, here's a new test case that should detect the change in the `digits_sum` function:
```python
def test():
    # Test with a negative number
    assert order_by_points([-3, -2, -1, 0, 1, 2, 3]) == [-3, -2, -1, 0, 1, 2, 3]

    # Test with a positive number
    assert order_by_points([3, 2, 1, 0, 1, 2, 3]) == [0, 1, 1, 2, 2, 3, 3]

    # Test with a mixed bag of positive and negative numbers
    assert order_by_points([-2, -1, 0, 1, 2, 3, 4]) == [-4, -3, -2, -1, 0, 1, 2]
```
This test case creates three lists of numbers with different signs and sizes, and then calls the `order_by_points` function on each of