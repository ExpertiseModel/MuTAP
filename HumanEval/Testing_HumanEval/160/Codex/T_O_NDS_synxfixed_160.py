def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)

def test():
    assert do_algebra(['+', '-'], [1, 2, 3, 4]) == -5, '-'
    assert do_algebra(['+', '-', '*', '/'], [1, 2, 3, 4]) == 0.5, '/'
    assert do_algebra(['+', '-', '*', '/'], [1, 2, 3, 4, 5]) == 4, '/'
    assert do_algebra(['+', '-', '*', '^'], [1, 2, 3, 4, 5]) == eval('1**3+2**2+3**1+4**0'), '^'
    