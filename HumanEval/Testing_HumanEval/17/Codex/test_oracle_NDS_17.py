from typing import List


def parse_music(music_string: str) -> List[int]:
    
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]



def test():
    assert parse_music('o  oo|o') == [4, 2, 4]
    assert parse_music('.|. .|') == [1, 1, 1]
# test()
