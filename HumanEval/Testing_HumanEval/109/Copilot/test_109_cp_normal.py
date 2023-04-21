from script_109_cp_normal  import move_one_ball
def test_move_one_ball():
    assert move_one_ball([1, 2, 3, 4, 5]) == True
    assert move_one_ball([5, 4, 3, 2, 1]) == True
    assert move_one_ball([1, 2, 3, 5, 4]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == True
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == True
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]) == False
    assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16]) == False