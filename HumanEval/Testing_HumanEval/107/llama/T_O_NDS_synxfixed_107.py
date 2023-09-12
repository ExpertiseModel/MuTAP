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


# test case
def test():

    assert even_odd_palindrome(10) == (5, 0)
    assert even_odd_palindrome(20) == (10, 0)
    assert even_odd_palindrome(30) == (15, 0)

    assert even_odd_palindrome(20) == (0, 5)
    assert even_odd_palindrome(30) == (0, 10)
    assert even_odd_palindrome(40) == (0, 15)

    assert even_odd_palindrome(5) == (2, 0)
    assert even_odd_palindrome(10) == (5, 0)
 