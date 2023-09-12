def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]
assert compare( [1, 2, 3], [2, 3, 4]) == [1, 1, 1]
