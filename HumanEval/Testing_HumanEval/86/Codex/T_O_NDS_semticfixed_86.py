def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


def test():
    assert anti_shuffle('a b c d') == 'a b c d'
    assert anti_shuffle('1 2 3 4') == '1 2 3 4'
    assert anti_shuffle('abcd efg hijkl mno') == 'abcd efg hijkl mno'
