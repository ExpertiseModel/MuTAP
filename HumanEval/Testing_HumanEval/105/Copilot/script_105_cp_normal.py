def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
    """
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

 # generate test case for the function above
def test_by_length():
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        "Nine",
        "Eight",
        "Seven",
        "Six",
        "Five",
        "Four",
        "Three",
        "Two",
        "One",
    ]
    assert by_length([1, 3, 5, 7, 9]) == [
        "Nine",
        "Seven",
        "Five",
        "Three",
        "One",
    ]
    assert by_length([2, 4, 6, 8]) == [
        "Eight",
        "Six",
        "Four",
        "Two",
    ]
    assert by_length([5, 6, 8, 9]) == [
        "Nine",
        "Eight",
        "Six",
        "Five",
    ]
    assert by_length([1, -1, 55]) == ["One"]
    assert by_length([0, 1, 2]) == ["Two", "One"]