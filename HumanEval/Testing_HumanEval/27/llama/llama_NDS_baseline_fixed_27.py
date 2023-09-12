def flip_case(string: str) -> str:
    
    return string.swapcase()




# test case

def test():
    assert flip_case("") == ""
    assert flip_case("hello") == "HELLO"
