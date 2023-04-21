def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def test():
    assert is_bored('I Like Java. Yeah!') == 1
    assert is_bored('I Like Python. I Like C++. I Like C#.') == 2
    
    
# run test
test()
