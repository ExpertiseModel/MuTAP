def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]


#</code>
#<test>

def test():
    assert eat(0, 0, 0) == [ 0, 0 ]
    assert eat(1, 0, 0) == [ 1, 0 ]
    assert eat(0, 1, 0) == [ 0, 0 ]
    assert eat(0, 0, 1) == [ 0, 1 ]
