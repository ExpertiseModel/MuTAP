def strlen(string: str) -> int:
    
    return len(string)




#</original code>


#<test>



def test():
    assert strlen("Hello") == 5
    assert strlen("World") == 5
    assert strlen("") == 0
    assert strlen("a") == 1
    assert strlen("aa") == 2
    assert strlen(None) == 0