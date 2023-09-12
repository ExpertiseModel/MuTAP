from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    
    return [x for x in strings if substring in x]


assert filter_by_substring(['hello', 'world', 'abc'], 'abc') == ['abc']
