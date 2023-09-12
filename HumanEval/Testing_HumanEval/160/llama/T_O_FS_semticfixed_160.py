def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


#</code>
#<test>

def test():
    assert do_algebra("+", [2, 3, 4]) == 5


    assert do_algebra("*", [2, 3, 4]) == 6


    assert do_algebra("^", [3, 4]) == 7

