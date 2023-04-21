def truncate_number(number: float) -> float:
    
    return number % 1.0



def test():
    assert truncate_number(6.0) == 0.0
    assert truncate_number(6.1) == 0.1
#</test>

