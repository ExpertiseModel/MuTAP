def truncate_number(number: float) -> float:
    
    return number % 1.0






def test():
    assert truncate_number(0.1) == 0.1
    assert truncate_number(1.1) == 0.10000000000000009
    assert truncate_number(-0.1) == 0.9
    assert truncate_number(2.3) == 0.2999999999999998
    assert truncate_number(3.7) == 0.7000000000000002
    assert truncate_number(-3.7) == 0.2999999999999998
    assert truncate_number(4.5) == 0.5
    assert truncate_number(-4.5) == 0.5
