def truncate_number(number: float) -> float:
    
    return number % 1.0




def test():
    assert truncate_number(0.1) == 0.1
    assert truncate_number(0.12) == 0.12
