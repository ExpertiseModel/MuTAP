def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum((sentence[0:] == 'I ' for sentence in sentences))
