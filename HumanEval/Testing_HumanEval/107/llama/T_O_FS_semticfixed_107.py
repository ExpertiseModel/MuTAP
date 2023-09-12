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
    assert even_odd_palindrome(2) == (1, 1)
    assert even_odd_palindrome(4) == (2, 2)
    assert even_odd_palindrome(6) == (3, 3)
    assert even_odd_palindrome(8) == (4, 4)
    assert even_odd_palindrome(10) == (4, 5)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(14) == (4, 6)
    assert even_odd_palindrome(16) == (4, 6)
    assert even_odd_palindrome(18) == (4, 6)
    assert even_odd_palindrome(20) == (4, 6)
