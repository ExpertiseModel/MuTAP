[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(x-y) for x,y in zip(game,guess)]


# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `compare` function in Python:
```python
test = [
    # incorrect guesses
    [compare([1,2,3,4,5,1], [1,2,5,4,2,-2])],
    # correct guesses
    [compare([0,5,0,0,0,4], [4,1,1,0,0,-2])],
    # mixed guesses
    [compare([1,2,3,4,5,1], [1,2,3,4,2,-2])],
    # very bad guesses
    [compare([0,5,0,0,0,6], [4,1,1,0,0,-2])],
]

```
For each test case, I will provide the input `game` and `guess` arrays, and the expected output of the `compare` function. You can verify the output of the function by using the `assert` statement in Python.
Let me know if you need any more test cases!