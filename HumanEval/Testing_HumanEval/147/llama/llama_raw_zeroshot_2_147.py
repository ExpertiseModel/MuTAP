[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `get_max_triples()` function:
1. `n = 1`:
Test case: `assert len(get_max_triples(1)) == 0`
Explanation: When `n = 1`, there are no valid triples, so the function should return 0.
Python code: `assert len(get_max_triples(1)) == 0`
2. `n = 2`:
Test case: `assert get_max_triples(2) == 1`
Explanation: When `n = 2`, there is only one valid triple: `(1, 2)`, so the function should return 1.
Python code: `assert get_max_triples(2) == 1`
3. `n = 3`:
Test case: `assert get_max_triples(3) == 2`
Explanation: When `n = 3`, there are two valid triples: `(1, 2, 3)` and `(2, 3, 1)`, so the function should return 2.
Python code: