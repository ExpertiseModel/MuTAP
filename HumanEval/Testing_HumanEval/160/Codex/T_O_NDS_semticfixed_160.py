def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


def test():
    assert do_algebra(['+', '-'], [1, 2, 3, 4]) == 0
    assert do_algebra(['+', '-', '*', '/'], [1, 2, 3, 4]) == -9
    assert do_algebra(['+', '-', '*', '/'], [1, 2, 3, 4, 5]) == 0.6000000000000001
    assert do_algebra(['+', '-', '*', '^'], [1, 2, 3, 4, 5]) == -14
