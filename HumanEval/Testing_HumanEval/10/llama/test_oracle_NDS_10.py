def is_palindrome(string: str) -> bool:
    
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]




# test case
def test():
    # Test with simple string
    assert make_palindrome('racecar') == 'racecar'
    # Test with longer string
    assert make_palindrome('The quick brown fox jumps over the lazy dog') == 'The quick brown fox jumps over the lazy dog'
    # Test with empty string
    assert make_palindrome('') == ''
    # Test with string that is not palindrome
    assert not make_palindrome('not a palindrome') == 'not a palindrome'
```