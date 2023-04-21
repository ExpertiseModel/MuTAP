def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above

def test_strlen():
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('a') == 1
    assert strlen('ab') == 2