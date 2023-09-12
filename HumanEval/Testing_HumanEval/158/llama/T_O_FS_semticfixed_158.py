def find_max(words):
   
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]


#</code>
#<test>

def test():
    assert find_max(["hello", "world", "abc", "def", "ghi", "jkl"]) == "world"

    assert find_max(["a", "b", "a", "c", "c", "d"]) == "a"
#</code>
    assert find_max(["a", "b", "a", "c", "d"]) == "a"
    assert find_max(["name", "of", "string"]) == "string"
    
    assert find_max(["rock", "paper", "scissors"]) == "scissors"

