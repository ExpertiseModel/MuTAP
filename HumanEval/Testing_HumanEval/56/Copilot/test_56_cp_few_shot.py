from script_56_cp_few_shot import correct_bracketing


def test_correct_bracketing():
    assert correct_bracketing("<") == False
    assert correct_bracketing("") == True
    assert correct_bracketing("><") == False
    assert correct_bracketing("<<>>") == True
    assert correct_bracketing("<<><") == False
    assert correct_bracketing("<><") == False
    assert correct_bracketing("<<><>>") == True
    assert correct_bracketing("<><>") == True
    assert correct_bracketing("<><<>") == False
    assert correct_bracketing("<><<>>") == True
    assert correct_bracketing("<><<>>") == True
    assert correct_bracketing("<<><<>>") == True
    assert correct_bracketing("<<><<>>>") == False
    assert correct_bracketing("<<<><<>>>") == False
    assert correct_bracketing("<<<><<>>><") == False
    assert correct_bracketing("<<<><<>>><>") == False
    assert correct_bracketing("<<<><<>>><><") == False
    assert correct_bracketing("<<<><<>>><><>") == False
    assert correct_bracketing("<<<><<>>><><><") == False
    assert correct_bracketing("<<<><<>>><><><>") == False