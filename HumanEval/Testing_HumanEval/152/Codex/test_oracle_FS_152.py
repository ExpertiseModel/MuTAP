def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]

def test():

def test():
    assert compare([1,2,3,4,5],[4,5,6,7,8]) == [1,1,1,1,1]
    assert compare([1,2,3,4,5],[8,7,6,5,4]) == [2,2,2,2,2]
    assert compare([1,2,3,4,5],[7,8,9,10,11]) == [3,3,3,3,3]
    assert compare([1,2,3,4,5],[4,5,6,7,8]) == [0,0,0,0,0]

