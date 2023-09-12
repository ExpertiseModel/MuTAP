def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


# test case

   

def test():
    # Test with a simple game
    assert compare( [1, 2, 3], [2, 3, 4]) == [1, 1, 1]

    # Test with a more complex game
    assert compare([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [2, 2, 2, 2, 2]

    # Test with different lengths
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test with invalid input
