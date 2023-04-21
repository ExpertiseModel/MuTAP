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
    assert by_length([1,4,3,2]) == ['One', 'Four', 'Three', 'Two'], "Charaters should be in the same order as the original array"
    assert by_length([0,6,7,7,9,10,13,0]) == [0, 'Seven', 'Nine', 'Ten', 'Zero', 'Zero', 'Zero', 'Zero'], "Zero should be the first in the new array"
    assert by_length([1,1,5,5,5,5,5,5,5,5,5]) == ['Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'One'], "Five should be lined up"
    assert by_length([2,2,2,2,2,2,2,2,2,2