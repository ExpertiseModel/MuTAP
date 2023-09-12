def compare(game,guess):
    
    return [abs(x-y) for x,y in zip(game,guess)]


#</code>
#<test>

def test():
    # Test with two equal lists
    
    assert compare([1, 2, 3],  [1, 2, 3]) == [0, 0, 0]
    # Test with two lists of different lengths
    
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    # Test with a list of integers and a list of floats
    
    assert compare([1, 2, 3], [4.0, 5.0, 6.0]) == [3.0, 3.0, 3.0]
    # Test with a list of integers and a list of lists
    game = [1, 2, 3]
    guess = [[4.0, 5.0, 6.0], [7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]
   
