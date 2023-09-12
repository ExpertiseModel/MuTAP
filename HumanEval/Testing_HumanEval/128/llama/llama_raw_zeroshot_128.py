[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def prod_signs(arr):
    
    if not arr: 
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `prod_signs` function:
1. Test with a positive array:
```
arr = [1, 2, 3, 4]
assert prod_signs(arr) == 24
```
2. Test with a negative array:
```
arr = [-1, -2, -3, -4]
assert prod_signs(arr) == -216
```
3. Test with an empty array:
```
arr = []
assert prod_signs(arr) == None
```
4. Test with an array containing only zeros:
```
arr = [0] * 5
assert prod_signs(arr) == 0
```
5. Test with an array containing only positives:
```
arr = [1, 2, 3, 4, 5]
assert prod_signs(arr) == 120
```
6. Test with an array containing only negatives:
```
arr = [-1, -2, -3, -4, -5]
assert prod_signs(arr) == -