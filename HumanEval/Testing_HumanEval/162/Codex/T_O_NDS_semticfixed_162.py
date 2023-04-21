def string_to_md5(text):
    
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


def test():
    assert string_to_md5('') == None
    assert string_to_md5('The quick brown fox jumps over the lazy dog') == '9e107d9d372bb6826bd81d3542a419d6'
