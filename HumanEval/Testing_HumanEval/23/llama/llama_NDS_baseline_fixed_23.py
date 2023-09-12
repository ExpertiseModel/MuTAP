def strlen(string: str) -> int:
    
    return len(string)




# test case

def test():
    assert strlen("") == 0
    assert strlen("hello") == 5
    assert strlen("a") == 1
    assert strlen({}) == 0
