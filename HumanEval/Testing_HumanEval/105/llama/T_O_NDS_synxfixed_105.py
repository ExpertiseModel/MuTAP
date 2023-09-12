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


# test case
def test():

    assert by_length([]) == []

    assert by_length([1, 2, 3]) == ['One', 'Two', 'Three']

    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']