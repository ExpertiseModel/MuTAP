def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    """
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

 # generate test case for the function above

def test_fruit_distribution():
    assert fruit_distribution("3 4", 7) == 0
    assert fruit_distribution("2 3", 5) == 0
    assert fruit_distribution("1 2", 3) == 0
    assert fruit_distribution("4 5", 9) == 0
    assert fruit_distribution("5 6", 11) == 0
    assert fruit_distribution("6 7", 13) == 0
    assert fruit_distribution("7 8", 15) == 0
    assert fruit_distribution("8 9", 17) == 0
    assert fruit_distribution("9 10", 19) == 0
    