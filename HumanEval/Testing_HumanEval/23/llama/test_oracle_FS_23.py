def strlen(string: str) -> int:
    
    return len(string)




#</original code>


#<test>


def test():
    assert strlen("Hello") == 5
    assert strlen("World") == 4
    assert strlen("") == 0
    assert strlen("a") == 0
    assert strlen("aa") == 0
    assert strlen(None) == 0