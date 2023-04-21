def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    """
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


METADATA = {}



 # generate test case for the function above

def test_correct_bracketing():
    assert correct_bracketing("<") == False
    assert correct_bracketing(">") == False
    assert correct_bracketing("<<") == False
    assert correct_bracketing(">>") == False
    assert correct_bracketing("<<<") == False
    assert correct_bracketing(">>>") == False
    assert correct_bracketing("<>") == True
    assert correct_bracketing("><") == False
    assert correct_bracketing("<><") == False
    assert correct_bracketing("><>") == False
    assert correct_bracketing("<><>") == True
    assert correct_bracketing("<><><") == False
    assert correct_bracketing("<><><") == False
    assert correct_bracketing("<><><>") == True
    assert correct_bracketing("<><><><") == False
    assert correct_bracketing("<><><><>") == True
    assert correct_bracketing("<><><><><") == False
    assert correct_bracketing("<><><><><>") == True
   