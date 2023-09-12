
def correct_bracketing(brackets: str):
    
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0




# test case
def test():
   
    # Test with valid brackets
    assert correct_bracketing("(()") == True
    assert correct_bracketing("(() {}") == True
    assert correct_bracketing("(()[]") == False
    assert correct_bracketing("(()[[])") == False
    # Test with invalid brackets
    assert correct_bracketing("())") == False
    assert correct_bracketing("([())") == False
    assert correct_bracketing("{())") == False
    assert correct_bracketing("(() {") == False
    
    # Test with very shallow brackets
    assert correct_bracketing("((") == False
    assert correct_bracketing("(()") == True
    assert correct_bracketing("((((()))))") == False
    # Test with very deep brackets
    assert correct_bracketing("((") == True
    assert correct_bracketing("((((()))))") == True 