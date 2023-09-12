def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)


#</original code>


#<test>
def test():
    assert is_bored("") == 1
    assert is_bored("I am curious about life, but bored with the weather. I love kittens, but I am not sure about this essay.") == 3
    assert is_bored("I am so bored.") == 1
    assert is_bored("I'm bored.") == 1
    assert is_bored("I'm really bored.") == 1
    assert is_bored("I'm super bored.") == 0
    assert is_bored("I'm not bored.") == 0