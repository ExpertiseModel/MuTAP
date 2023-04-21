from typing import List
from typing import List
#<code> 
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
#</code>
#<test>
def test_equilateral_triangle():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>
#<code>
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>
#<test>
def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>
#<code>
from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    """
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]





#</code>
#<test>

def test_parse_music():
    assert parse_music("o o o o") == [4, 4, 4, 4]
    assert parse_music("o| o| o| o|") == [2, 2, 2, 2]
    assert parse_music(".| .| .| .|") == [1, 1, 1, 1]
    assert parse_music("o o| o o|") == [4, 2, 4, 2]
    assert parse_music("o| o o| o") == [2, 4, 2, 4]
    assert parse_music("o o| o| o") == [4, 2, 2, 4]
    assert parse_music("o| o| o o") == [2, 2, 4, 4]
    assert parse_music("o o o| o|") == [4, 4, 2, 2]
    assert parse_music("o| o| o| o") == [2, 2, 2, 4]
    assert parse_music("o| o o o|") == [2, 4, 4, 2]
    assert parse_music("o| o o| o") == [2, 4, 2, 4]
    assert parse_music("o o| o o") == [4, 2, 4, 4]
    assert parse_music("o o o o|") == [4, 4, 4, 2]
    assert parse_music("o o o| o") == [4, 4, 2, 4]
    assert parse_music("o| o o o") == [2, 4, 4, 4]
    assert parse_music("o o| o| o|") == [4, 2, 2, 2]
    assert parse_music("o| o| o| o|") == [2, 2, 2, 2]

