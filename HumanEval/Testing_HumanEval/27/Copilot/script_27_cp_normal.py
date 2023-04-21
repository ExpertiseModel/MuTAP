def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    """
    return string.swapcase()


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}



 # generate test case for the function above

def test_flip_case():
    assert flip_case('') == ''
    assert flip_case('a') == 'A'
    assert flip_case('A') == 'a'
    assert flip_case('abc') == 'ABC'
    assert flip_case('ABC') == 'abc'
    assert flip_case('aBc') == 'AbC'
    assert flip_case('AbC') == 'aBc'
    assert flip_case('aBc123') == 'AbC123'
    assert flip_case('AbC123') == 'aBc123'
    assert flip_case('aBc123!') == 'AbC123!'
    assert flip_case('AbC123!') == 'aBc123!'
    assert flip_case('aBc123!@#') == 'AbC123!@#'
    assert flip_case('AbC123!@#') == 'aBc123!@#'
    assert flip_case('aBc123!@#_') == 'AbC123!@#_'
    assert flip_case('AbC123!@#_') == 'aBc123!@#_'
    assert flip_case('aBc123!@#_ ') == 'AbC123!@#_ '
    assert flip_case('AbC123!@#_ ') == 'aBc123!@#_ '
    assert flip_case('aBc123!@#_  ') == 'AbC123!@#_  '
    assert flip_case('AbC123!@#_  ') == 'aBc123!@#_  '
    assert flip_case('aBc123!@#_   ') == 'AbC123!@#_   '
    assert flip_case('AbC123!@#_   ') == 'aBc123!@#_   '
    assert flip_case('aBc123!@#_    ') == 'AbC123!@#_    '
    assert flip_case('AbC123!@#_    ') == 'aBc123!@#_    '
    assert flip_case('aBc123!@#_     ') == 'AbC123!@#_     '

