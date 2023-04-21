from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    
    return [x for x in strings if x.startswith(prefix)]




def test():
    assert filter_by_prefix(['hello', 'file', 'world', 'file2'], "fi") == ["file", "file2"]
    assert filter_by_prefix(['hello', 'file', 'world', 'file2'], "ho") == []
    assert filter_by_prefix(['hello', 'file', 'world', 'file2'], "fil") == ["file", "file2"]
    assert filter_by_prefix(['hello', 'file', 'world', 'file2'], "wo0") == []
    assert filter_by_prefix(['hello', 'file', 'world', 'file2'], "") == ['hello', 'file', 'world', 'file2']
