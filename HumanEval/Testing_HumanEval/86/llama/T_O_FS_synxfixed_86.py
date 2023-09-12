def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


#</code>
#<test>
def test():
  
    assert anti_shuffle("Hello").lower() == "HLLO"
    assert anti_shuffle("World").lower() == "WRLD"
    assert anti_shuffle("Python").lower() == "PTHN"
    assert anti_shuffle("List").lower() == "LST"
    assert anti_shuffle("Random").lower() == "NDMRND"
    assert anti_shuffle("Shuffle").lower() == "SHFD"
    # Test edge cases
    assert anti_shuffle("").lower() == ""
    assert anti_shuffle("   ").lower() == "   "
    assert anti_shuffle("  ").lower() == "  "
    # Test input of different types
    assert anti_shuffle(1).lower() == "1"
    assert anti_shuffle(True).lower() == "T"
    assert anti_shuffle([1, 2, 3]).lower() == "123"
    #