def string_sequence(n: int) -> str:
    
    return ' '.join([str(x) for x in range(n + 1)])


assert string_sequence(1) == '0 1'
