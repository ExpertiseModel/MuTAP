def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def test():
    assert string_to_md5("") == 
    assert string_to_md5("The quick brown fox jumps over the lazy dog") == 
    assert string_to_md5("Nobody inspects the spammish repetition") == 
    assert string_to_md5("The quick brown fox jumps over the lazy cog") == 
    assert string_to_md5("Nobody expects the spammish zener zen") == 
