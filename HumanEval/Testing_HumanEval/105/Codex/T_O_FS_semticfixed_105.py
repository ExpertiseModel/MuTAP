def by_length(arr):
    
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr


def test():
    assert by_length([0, 2, 1, 2]) == ['Two', 'Two', 'One']
    assert by_length([0, 2, 1, 2]) == ['Two', 'Two', 'One']
    assert by_length([1, 2, 1, 4]) == ['Four', 'Two', 'One', 'One']
    assert by_length([10, 20, 2, 3, 2, 3, 2, 20, 2, 1, 2]) == ['Three', 'Three', 'Two', 'Two', 'Two', 'Two', 'Two', 'One']
    assert by_length([2, 3, 2, 3]) == ['Three', 'Three', 'Two', 'Two']
