def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    
    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n+1):
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)

 # generate test case for the function above
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