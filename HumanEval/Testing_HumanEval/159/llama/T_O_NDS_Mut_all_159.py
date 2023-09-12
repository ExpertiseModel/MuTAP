def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]


# test case

def test():
    assert eat(10, 5, 15) == [10 + 5, 10]


    assert eat(-5, 10, 20) == [5, 10]

    assert eat(10, -5, 15) == [5, 20]

    assert eat(10, 20, 10) == [20, 0]

    assert eat(0, 0, 0) == [0, 0]

    assert eat(-5, 10, 20) == [5, 10]
    assert eat(10, 5, 15) == [10 + 5, 10]

    # Case 2: need is greater than or equal to remaining
    assert eat(10, 10, 10) == [10, 0]

    # Case 3: need is greater than remaining
    assert eat(10, 20, 15) == [5, 15]

    # Case 4: need is less than remaining and the function returns a list
    assert eat(-5, 10, 20) == [5, 10]
