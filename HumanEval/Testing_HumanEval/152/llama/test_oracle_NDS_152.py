def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


# test case

   
def test():
    # Test with a simple game
    assert compare( [1, 2, 3], [2, 3, 4]) == [1, 1, 0]

    # Test with a more complex game
    assert compare([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) == [2, 1, 0, 0, 0]

    # Test with different lengths
    assert compare([1, 2, 3], [4, 5, 6]) == [1, 1, 0]

    # Test with invalid input
    game = [1, 2, 3]
    guess = [4, 5, 6, 7]
    result