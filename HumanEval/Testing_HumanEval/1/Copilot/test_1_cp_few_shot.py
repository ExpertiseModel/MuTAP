from script_1_cp_few_shot import separate_paren_groups

def test_separate_paren_groups():
    assert separate_paren_groups("()") == ["()"]
    assert separate_paren_groups("()()") == ["()", "()"]
    assert separate_paren_groups("(())") == ["(())"]
    assert separate_paren_groups("((()))") == ["((()))"]
    assert separate_paren_groups("((())())") == ["((())())"]
    assert separate_paren_groups("((())())()") == ["((())())", "()"]
    assert separate_paren_groups("((())())()()") == ["((())())", "()", "()"]


test_separate_paren_groups()