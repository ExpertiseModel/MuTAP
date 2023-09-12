def flip_case(string: str) -> str:
    
    return string.swapcase()




# test case

def test():
    #test_flip_case_empty_string
    assert flip_case("") == ""

    #test_flip_case_lowercase_string
    assert flip_case("hello") == "HELLO"

   #test_flip_case_mixed_case_string
    assert flip_case("HeLlO") == "hElLo"

    #test_flip_case_correct_case
    assert flip_case("UpPerCASE") == "uPpERcase"
