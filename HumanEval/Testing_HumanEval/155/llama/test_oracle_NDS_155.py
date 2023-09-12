def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)


# test case
def test():
   
    # Test even count

    assert even_odd_count(12) == (3, 0)

    # Test odd count
    assert even_odd_count(13) == (0, 3)

    # Test edge cases

    assert even_odd_count(-1) == (0, 0)

    # Test invalid input

    assert even_odd_count(" Hello, world!") == (0, 0)

# Test multiple inputs
    nums = [12, 13, 14]
    results = [even_odd_count(num) for num in nums]
    assert all(result[0