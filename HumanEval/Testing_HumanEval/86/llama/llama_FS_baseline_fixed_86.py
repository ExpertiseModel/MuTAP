def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


#</code>
#<test>

def test():
    assert anti_shuffle("").lower() == ""
    assert anti_shuffle("   ").lower() == "   "
    assert anti_shuffle("  ").lower() == "  "
