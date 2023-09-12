
def find_max(words):
   
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]


# test case

def test():
    # Test 1: Ensure the function returns the maximum length word
    assert find_max(['hello', 'world', 'hello', 'universe', 'universe', 'hello']) == 'universe'

    # Test 2: Ensure the function sorts the words correctly
    assert sorted(['universe', 'hello', 'world', 'hello', 'goodbye'], key=find_max) == ['goodbye', 'world', 'universe', 'hello', 'hello']

    # Test 3: Ensure the function works with empty inputs
    assert find_max([]) == ''
    # Test 4: Ensure the function works with inconsistent inputs
    assert find_max(wwords = ['hello', 'world', 'hello']) == 'hello'
   
    assert sorted(['universe', 'hello', 'world', 'hello', 'goodbye'], key=find_max) == ['goodbye', 'world', 'universe', 'hello', 'hello']

