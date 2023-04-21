def fib4(n: int):
    
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]





def test():
    Traceback (most recent call last):
        File "Fibonacci-test.py", line

        print(fib4(2))
    File "<stdin>", line 5, in <module>
    assert fib4(2) == 2
    AssertionError
    """
    assert fib4(5) == 4
    """
    Traceback (most recent call last):
        File "Fibonacci-test.py", line
    
        assert fib4(5) == 4
    File "<stdin>", line 5, in <module>
    AssertionError
    """
    assert fib4(6) == 8
    """
    Traceback (most recent call last):
        File "Fibonacci-test.py", line
        assert fib4(6) == 8
    File "<stdin>", line 5, in <