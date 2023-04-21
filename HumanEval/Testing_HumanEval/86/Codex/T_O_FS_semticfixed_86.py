def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


def test():
    assert anti_shuffle('1 2 3 4 5 6') == 1 2 3 4 5 6
    assert anti_shuffle('1 2 3 4 5 6 7 8') == 1 2 3 4 5 6 7 8
    assert anti_shuffle('1 2 3 4 5 6 7 8 9') == 1 2 3 4 5 6 7 8 9
