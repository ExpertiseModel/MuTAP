def find_max(words):
   
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]

def test():
    
   
    
    assert find_max(['abc', 'abc', 'abc', 'abc']) == 'abc'
    assert find_max(['abc', 'bca', 'cba', 'abc']) == 'abc'
    assert find_max(['abc', 'cba', 'bca', 'abc']) == 'abc'
    assert find_max(['abc', 'cba', 'aac', 'aac']) == 'aac'
    assert find_max(['aaa', 'bca', 'aac', 'aac']) == 'aaa'
    
    
    
    
    
    
    
    
    
    
    
    assert