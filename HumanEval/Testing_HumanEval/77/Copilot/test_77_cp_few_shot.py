from script_77_cp_few_shot import iscube


def test_iscube():
    assert iscube(1) == True
    assert iscube(8) == True
    assert iscube(27) == True
    assert iscube(64) == True
    assert iscube(125) == True
    assert iscube(216) == True
    assert iscube(343) == True
    assert iscube(512) == True
    assert iscube(729) == True
    assert iscube(1000) == True
    assert iscube(1331) == False
    assert iscube(0) == True
    assert iscube(-1) == True
    assert iscube(-8) == True
    assert iscube(-27) == True
    assert iscube(-64) == True
    assert iscube(-125) == True
    assert iscube(-216) == True
    assert iscube(-343) == True


