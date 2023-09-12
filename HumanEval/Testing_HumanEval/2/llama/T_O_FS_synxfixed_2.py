def truncate_number(number: float) -> float:
    
    return number % 1.0





def test():
    assert truncate_number(0.1) == 0.1
    assert truncate_number(1.1) == 1.0
    assert truncate_number(-0.1) == -0.1
    assert truncate_number(2.3) == 2.0
    assert truncate_number(3.7) == 3.0
    assert truncate_number(-3.7) == -3.0
    assert truncate_number(4.5) == 4.0
    assert truncate_number(-4.5) == -4.0