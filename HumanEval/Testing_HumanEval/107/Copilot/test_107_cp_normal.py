from script_107_cp_normal import even_odd_palindrome
def test_even_odd_palindrome():
    assert even_odd_palindrome(10) == (2, 1)
    assert even_odd_palindrome(20) == (4, 2)
    assert even_odd_palindrome(30) == (6, 3)
    assert even_odd_palindrome(40) == (8, 4)
    assert even_odd_palindrome(50) == (10, 5)
    assert even_odd_palindrome(60) == (12, 6)
    assert even_odd_palindrome(70) == (14, 7)
    assert even_odd_palindrome(80) == (16, 8)
    assert even_odd_palindrome(90) == (18, 9)
    assert even_odd_palindrome(100) == (20, 10)