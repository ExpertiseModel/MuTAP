from typing import List


def all_prefixes(string: str) -> List[str]:
    
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result





def test():
    assert all_prefixes("hello") == ['h', 'he', 'hel', 'hell', 'hello']

    assert all_prefixes("") == []

    assert  all_prefixes("a") == ["a"]

    assert all_prefixes("banana") == ['b', 'ba', 'ban', 'bana', 'banan', 'banana']


    assert  all_prefixes("hello") == ['h', 'he', 'hel', 'hell', 'hello']

    assert all_prefixes("the quick brown fox") == ['t', 'th', 'the', 'the ', 'the q', 'the qu', 'the qui', 'the quic', 'the quick', 'the quick ', 'the quick b', 'the quick br', 'the quick bro', 'the quick brow', 'the quick brown', 'the quick brown ', 'the quick brown f', 'the quick brown fo', 'the quick brown fox']

    assert all_prefixes("the quick brown   fox") == ['t', 'th', 'the', 'the ', 'the q', 'the qu', 'the qui', 'the quic', 'the quick', 'the quick ', 'the quick b', 'the quick br', 'the quick bro', 'the quick brow', 'the quick brown', 'the quick brown ', 'the quick brown  ', 'the quick brown   ', 'the quick brown   f', 'the quick brown   fo', 'the quick brown   fox']
