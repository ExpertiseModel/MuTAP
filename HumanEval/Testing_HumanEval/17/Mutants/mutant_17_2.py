from typing import List


def parse_music(music_string: str) -> List[int]:
    
    note_map = {'o': 4, 'o|': 2, '.|': 0}
    return [note_map[x] for x in music_string.split(' ') if x]



