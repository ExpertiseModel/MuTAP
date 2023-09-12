
def fib4(n: int):
    
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]




# test case
def test():

    assert fib4(3) == 2

    assert fib4(0) == 0

    assert fib4(14) == 6765

    assert fib4(-3) == -2

    assert fib4(50) == None
