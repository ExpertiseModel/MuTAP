from typing import List


def concatenate(strings: List[str]) -> str:
    
    return ''.join(strings)




#</code>
#<test>

def test():
    assert concatenate([]) == ""
    assert concatenate(['hello']) == "hello"
