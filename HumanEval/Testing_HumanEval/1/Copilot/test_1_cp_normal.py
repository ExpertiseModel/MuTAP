from script_1_cp_few_shot import separate_paren_groups
def generate_test_case():
    assert separate_paren_groups('()') == ['()']
    assert separate_paren_groups('(())') == ['(())']
    assert separate_paren_groups('((()))') == ['((()))']
    assert separate_paren_groups('()()') == ['()', '()']
    assert separate_paren_groups('(()())') == ['(()())']
    assert separate_paren_groups('((()))()') == ['((()))', '()']
    assert separate_paren_groups('((())())') == ['((())())']
    assert separate_paren_groups('((())())((()))') == ['((())())', '((()))']
    assert separate_paren_groups('((())())((()))()') == ['((())())', '((()))', '()']
    assert separate_paren_groups('((())())((()))()()') == ['((())())', '((()))', '()', '()']