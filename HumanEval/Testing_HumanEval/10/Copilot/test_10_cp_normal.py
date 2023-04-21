from script_10_cp_few_shot import make_palindrome
def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('a') == 'a'
    assert make_palindrome('ab') == 'aba'
    assert make_palindrome('abc') == 'abcba'
    assert make_palindrome('abcd') == 'abcdcba'
    assert make_palindrome('abcde') == 'abcdeedcba'
    assert make_palindrome('abcdef') == 'abcdeffedcba'
    assert make_palindrome('abcdefg') == 'abcdefgfedcba'
    assert make_palindrome('abcdefgh') == 'abcdefghgfedcba'
    assert make_palindrome('abcdefghi') == 'abcdefghihgfedcba'