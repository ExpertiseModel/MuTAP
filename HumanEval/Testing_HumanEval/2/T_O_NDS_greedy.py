def truncate_number(number: float) -> float:
    
    return number % 1.0


assert truncate_number(1.1) == 0.10000000000000009
