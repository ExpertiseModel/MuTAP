from typing import List


def parse_music(music_string: str) -> List[int]:
    
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]




# test case

def test():
    #test_empty_music
    assert parse_music("   ") == []

    #test_single_note
    assert parse_music("o") == [4]

    #test_double_notes
    assert parse_music("o|.|") == [2, 1]
    #test_multi_notes
    assert parse_music(".o.|.o|") == [1, 2, 4]
    #test_mixed_notes
    assert parse_music("o.o|.|") == [2, 1, 4]
    #test_whitespace
    assert parse_music(" \to.| ") == [1, 2, 4]
    #test_empty_string
    assert parse_music("") == []
