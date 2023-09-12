def fib4(n: int):
    
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]




#</code>
#<test>
def test():
    assert fib4(4) == [0, 0, 2, 0]
    assert fib4(5) == [0, 0, 2, 0, 1]
    assert fib4(6) == [0, 0, 2, 0, 1, 1]
    assert fib4(7) == [0, 0, 2, 0, 1, 1, 2]
    assert fib4(8) == [0, 0, 2, 0, 1, 1, 2, 3]
    assert fib4(9) == [0, 0, 2, 0, 1, 1, 2, 3, 4]
    assert fib4(4) == [0, 0, 2, 0]

    assert fib4(10) == [0, 0, 2, 0, 3, 5, 8, 13, 21, 34]

    assert fib4(40) == [0, 0, 2, 0, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]