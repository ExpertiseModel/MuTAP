def truncate_number(number: float) -> float:
    
    return number % 1.0



 # generate test case for the function above

def test_truncate_number():
    assert truncate_number(1.0) == 0.0
    assert truncate_number(1.1) == 0.1
    assert truncate_number(1.2) == 0.2
    assert truncate_number(1.3) == 0.3
    assert truncate_number(1.4) == 0.4
    assert truncate_number(1.5) == 0.5
    assert truncate_number(1.6) == 0.6
    assert truncate_number(1.7) == 0.7
    assert truncate_number(1.8) == 0.8
    assert truncate_number(1.9) == 0.9
    assert truncate_number(1.99) == 0.99
    assert truncate_number(1.999) == 0.999
    assert truncate_number(1.9999) == 0.9999
    assert truncate_number(1.99999) == 0.99999
    assert truncate_number(1.999999) == 0.999999
    assert truncate_number(1.9999999) == 0.9999999
    assert truncate_number(1.99999999) == 0.99999999
    assert truncate_number(1.999999999) == 0.999999999
   