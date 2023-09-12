[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def count_nums(arr):
    
    def digits_sum(n):
        neg = 1
        if n < 0: 
            n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


# test case
def test():
    assert [/INST]  Sure, here are some test cases for the `count_nums` function:
Test Case 1: Positive Number
arr = [1, 2, 3, 4, 5]
Expected Output: 5
Actual Output: `assert len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr]))) == 5`
Test Case 2: Negative Number
arr = [-1, -2, -3, -4, -5]
Expected Output: 5
Actual Output: `assert len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr]))) == 5`
Test Case 3: Zero Number
arr = [0, 0, 0, 0, 0]
Expected Output: 0
Actual Output: `assert len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr]))) == 0`
Test Case 4: Non-Integer Number
arr = [1.5, 2