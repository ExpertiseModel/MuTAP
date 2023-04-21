from typing import List


def concatenate(strings: List[str]) -> str:
    
    return ''.join(strings)




def test():
    assert concatenate(['hello', 'world']) == 'helloworld'
    assert concatenate(['hello', 'world']) == 'helloworld'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', '']) == 'a'
    assert concatenate(['', 'a']) == 'a'
    assert concatenate(['']) == ''
    assert concatenate(None) == ''    
    assert concatenate(['', '', '']) == ''
