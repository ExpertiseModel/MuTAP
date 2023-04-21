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
    assert fib4(5) == 4
    assert fib4(12) == 386
    assert fib4(45) == 981302949796
    assert fib4(500) == 4683845716690180034539796272188497123185499535401362646845638880052842590096588363096828154816550799073811944964910934796641232183050271821520
    assert fib4(60) == 18489636016979440
