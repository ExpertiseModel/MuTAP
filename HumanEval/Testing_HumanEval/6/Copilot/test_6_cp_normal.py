from script_6_cp_few_shot import parse_nested_parens

def test_parse_nested_parens():
    assert parse_nested_parens('') == []
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('() ()') == [1, 1]
    assert parse_nested_parens('() () ()') == [1, 1, 1]
    assert parse_nested_parens('() () (())') == [1, 1, 2]
    assert parse_nested_parens('() () (()) ()') == [1, 1, 2, 1]
    assert parse_nested_parens('() () (()) () ()') == [1, 1, 2, 1, 1]
    assert parse_nested_parens('() () (()) () () ()') == [1, 1, 2, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () ()') == [1, 1, 2, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]
    assert parse_nested_parens('() () (()) () () () () () () () () ()') == [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]