from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    
    return [x for x in strings if x.startswith(prefix)]




def test():
    assert filter_by_prefix([], '') == ['']
    assert filter_by_prefix(['apple', 'banana', 'orange'], 'a') == ['apple']
    assert filter_by_prefix(['apple', 'banana', 'orange'], 'ba') == ['banana', 'orange']
    assert filter_by_prefix(['apple', 'banana', 'orange'], 'an') == ['apple', 'banana']
    assert filter_by_prefix(['apple', 'banana', 'orange'], 'or') == ['orange']
    assert filter_by_prefix(['apple', 'banana', 'orange'], 'al') == ['apple', 'orange']
    assert filter_by_prefix(['apple', 'banana', 'orange'], 'a') == ['apple']