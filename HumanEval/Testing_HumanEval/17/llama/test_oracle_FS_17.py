from typing import List


def parse_music(music_string: str) -> List[int]:
    
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]




def test():

    assert parse_music("o") == [4]

    assert parse_music("o|") == [2]

    assert parse_music("/.|..|.o.|.") == [1, 2, 4, 4, 1]

        # Test empty input
    assert parse_music("") == []
    # Test simple melody
    assert parse_music("o|.") == [4]
    assert parse_music("o.|.") == [2]
    # Test more complex melody
    assert parse_music("o|o|.") == [4, 4]
    assert parse_music("o.|o.|.") == [2, 2]
    # Test invalid input
    assert parse_music("x|y") == []
    assert parse_music("|z") == []
    assrt 
