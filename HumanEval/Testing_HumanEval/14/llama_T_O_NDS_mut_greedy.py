from typing import List


def all_prefixes(string: str) -> List[str]:
    
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result


assert all_prefixes("hello") == ['h', 'he', 'hel', 'hell', 'hello']
