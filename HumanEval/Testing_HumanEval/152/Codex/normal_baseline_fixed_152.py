def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


def test():
    assert len(compare([0,1,2],[2,2,2]))==3
