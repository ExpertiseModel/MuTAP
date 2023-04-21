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

def test():
`python
import unittest

class TestEvenOddPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(even_odd_palindrome(2), (0,1))
        self.assertEqual(even_odd_palindrome(3), (1,1))
        self.assertEqual(even_odd_palindrome(4), (1,2))
        self.assertEqual(even_odd_palindrome(5), (1,2))
        self.assertEqual(even_odd_palindrome(6), (1,2))
        self.assertEqual(even_odd_palindrome(7), (2,2))
        self.assertEqual(even_odd_palindrome(8), (3,3))
       