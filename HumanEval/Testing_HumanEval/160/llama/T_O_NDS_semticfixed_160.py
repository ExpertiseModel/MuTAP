
def do_algebra(operator, operand):
    
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+= oprt + str(oprn)
    return eval(expression)


# test case

def test():
    assert do_algebra("++", ["a", "b", "c"]) == "a+b+c"

    assert do_algebra("-+", ["a", "b", "c"]) == "-a-b-c"

    assert do_algebra("*", ["a", "b", "c"]) == "a*b*c"

    assert do_algebra("/",  []) == ""
   
