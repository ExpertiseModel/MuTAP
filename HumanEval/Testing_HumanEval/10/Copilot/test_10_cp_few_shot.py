from script_10_cp_few_shot import make_palindrome

def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('a') == 'a'
    assert make_palindrome('ab') == 'aba'
    assert make_palindrome('abc') == 'abccba'
    assert make_palindrome('abcd') == 'abcdcba'
    assert make_palindrome('abcde') == 'abcdeedcba'
