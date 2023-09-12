def even_odd_palindrome(n):
    
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


#</code>
#<test>
def test():
    
    assert even_odd_palindrome(2) == (1, 0)
    assert even_odd_palindrome(4) == (2, 0)
    assert even_odd_palindrome(6) == (3, 0)
    assert even_odd_palindrome(8) == (4, 0)
    assert even_odd_palindrome(10) == (5, 0)
    assert even_odd_palindrome(12) == (6, 0)
    assert even_odd_palindrome(14) == (7, 0)
    assert even_odd_palindrome(16) == (8, 0)
    assert even_odd_palindrome(18) == (9, 0)
    assert even_odd_palindrome(20) == (10, 0)