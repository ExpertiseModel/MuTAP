def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

def test():
    assert anti_shuffle('a b c d') == 'b c a d'
    assert anti_shuffle('1 2 3 4') == '4 2 3 1'
    assert anti_shuffle('abcd efg hijkl mno') == 'klmn hije fcdg ba'
