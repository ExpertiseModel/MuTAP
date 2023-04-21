def fib4(n: int):
    
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]



def test():
    assert fib4(2) == 2
    assert fib4(5) == 5
    assert fib4(12) == 144
    assert fib4(45) == 152265
    assert fib4(500) == 13940581
    assert fib4(60) == 151937
