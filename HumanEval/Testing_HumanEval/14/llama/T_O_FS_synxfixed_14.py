from typing import List


def all_prefixes(string: str) -> List[str]:
    
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result




def test():

    assert all_prefixes("hello") == ["hello"]

    assert all_prefixes("") == []

    assert  all_prefixes("a") == ["a"]

    assert all_prefixes("banana") == ["ban", "banana"]


    assert  all_prefixes("hello") == ["hello"]

    assert all_prefixes("the quick brown fox") == ["the", "the quick", "the quick brown", "the quick brown fox"]

    assert all_prefixes("the quick brown   fox") == ["the", "the quick", "the quick brown", "the quick brown   fox"]