from script_109_cp_normal  import move_one_ball
def test_move_one_ball():
    assert move_one_ball([1, 2, 3, 4, 5]) == True
    assert move_one_ball([5, 4, 3, 2, 1]) == True
    assert move_one_ball([1, 2, 3, 5, 4]) == True
    assert move_one_ball([1, 2, 3, 4, 4]) == False
    assert move_one_ball([1, 2, 2, 4, 5]) == False
    assert move_one_ball([1, 2, 2, 4, 4]) == False
    assert move_one_ball([1, 2, 3, 4, 6]) == False
    assert move_one_ball([1]) == True
    assert move_one_ball([]) == True
