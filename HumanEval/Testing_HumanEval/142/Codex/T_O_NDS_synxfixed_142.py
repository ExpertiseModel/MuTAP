def sum_squares(lst):
    
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

def test():
    assert sum_squares([1,2,3,4,5,6,7]) == 195
    assert sum_squares([1,2,3,5,6,7,8,9]) == 1530


if __name__ == "__main__":
    test()
