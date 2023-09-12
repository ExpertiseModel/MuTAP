def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


#</code>
#<test>
def test():
    
    
    assert do_algebra("+", [2, 3, 4]) == 9, "Addition operation failed"


    assert do_algebra("*", [2, 3, 4]) == 24, "Multiplication operation failed"


    assert do_algebra("^", [3, 4]) == 81, "Exponentiation operation failed"

    result = do_algebra("/", [8, 4]