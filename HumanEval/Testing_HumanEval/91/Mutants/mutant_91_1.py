def is_bored(S):
    
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum((sentence[:2] == 'I ' for sentence in sentences))
