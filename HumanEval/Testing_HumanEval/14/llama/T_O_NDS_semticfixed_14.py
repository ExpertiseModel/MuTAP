from typing import List


def all_prefixes(string: str) -> List[str]:
    
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result




# test case

def test():
    # Test that the function returns all the prefixes of a string
    assert all_prefixes("hello") == ['h', 'he', 'hel', 'hell', 'hello']

    # Test that the function works for different length strings
    assert all_prefixes("") == []
    assert all_prefixes("a") == ['a']
    assert all_prefixes("ab") == ['a', 'ab']

    # Test that the function returns the correct prefixes
    assert all_prefixes("hello") == ['h', 'he', 'hel', 'hell', 'hello']

    # Test that the function works for negative indices
    assert all_prefixes("hello", -1) == ['hello']    
    assert all_prefixes("hello", -2) == ['hello', 'hel']
    # Test that the function works for large strings
    assert all_prefixes("foobar") == ['f', 'fo', 'foo', 'foob', 'fooba', 'foobar']
