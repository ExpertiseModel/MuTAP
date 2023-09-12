[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))


# test case
def test():
    assert [/INST]  Great! I'd be happy to help you generate test cases for the `rounded_avg` function. Here are some test cases you can use:
1. Test that the function returns the correct value for small inputs:
    \begin{code}
    assert rounded_avg(1, 1) == '0b1'
    assert rounded_avg(2, 2) == '0b10'
    assert rounded_avg(3, 3) == '0b11'
    assert rounded_avg(4, 4) == '0b100'
    assert rounded_avg(5, 5) == '0b111'
\end{code}
2. Test that the function returns the correct value for medium-sized inputs:
    \begin{code}
    assert rounded_avg(10, 15) == '0b11110'
    assert rounded_avg(20, 25) == '0b110100'
    assert rounded_avg(30, 35) == '