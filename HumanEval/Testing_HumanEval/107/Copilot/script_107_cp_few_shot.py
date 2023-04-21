from typing import List
from typing import List
#<code> 
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
#</code>
#<test>
def test_equilateral_triangle():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>
#<code>
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>
#<test>
def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>
#<code>
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

#</code>
#<test>

#wait here to collect unit tests

def test_even_odd_palindrome():
    assert even_odd_palindrome(3) == (0, 1)
    assert even_odd_palindrome(4) == (1, 0)
    assert even_odd_palindrome(5) == (1, 1)
    assert even_odd_palindrome(6) == (2, 1)
    assert even_odd_palindrome(7) == (2, 2)
    assert even_odd_palindrome(8) == (3, 2)
    assert even_odd_palindrome(9) == (3, 3)
    assert even_odd_palindrome(10) == (4, 3)
    assert even_odd_palindrome(11) == (4, 4)
    assert even_odd_palindrome(12) == (5, 4)
    assert even_odd_palindrome(13) == (5, 5)
    assert even_odd_palindrome(14) == (6, 5)
    assert even_odd_palindrome(15) == (6, 6)
    assert even_odd_palindrome(16) == (7, 6)
    assert even_odd_palindrome(17) == (7, 7)
    assert even_odd_palindrome(18) == (8, 7)
    assert even_odd_palindrome(19) == (8, 8)
    assert even_odd_palindrome(20) == (9, 8)
    assert even_odd_palindrome(21) == (9, 9)
    assert even_odd_palindrome(22) == (10, 9)
    assert even_odd_palindrome(23) == (10, 10)
    assert even_odd_palindrome(24) == (11, 10)
    assert even_odd_palindrome(25) == (11, 11)
    assert even_odd_palindrome(26) == (12, 11)


