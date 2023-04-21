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




 # generate test case for the function above

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