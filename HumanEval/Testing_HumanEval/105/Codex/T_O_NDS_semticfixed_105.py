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
    assert by_length([1,4,3,2]) == ['Four', 'Three', 'Two', 'One']
    assert by_length([0,6,7,7,9,10,13,0]) == ['Nine', 'Seven', 'Seven', 'Six']
    assert by_length([1,1,5,5,5,5,5,5,5,5,5]) == ['Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'One', 'One']
