def truncate_number(number: float) -> float:
    
    return number % 1.0




def test():
    assert truncate_number(0.1) == 0.1
    assert truncate_number(1.1) == 0.10000000000000009
    assert truncate_number(0.12) == 0.12
    assert truncate_number(1.12) == 0.1200000000000001
    assert truncate_number(0.123) == 0.123
    assert truncate_number(1.123) == 0.123
    assert truncate_number(0.1234) == 0.1234
    assert truncate_number(1.1234) == 0.12339999999999995
    assert truncate_number(0.12345) == 0.12345
    assert truncate_number(1.12345) == 0.12345000000000006
    assert truncate_number(0.123456) == 0.123456
    assert truncate_number(1.123456) == 0.12345600000000001
