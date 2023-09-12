[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

 Generate test cases for the following function:
#original function
from typing import List


def parse_music(music_string: str) -> List[int]:
    
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]




# test case
def test():
    assert [/INST]  Sure! Here are some test cases for the `parse_music` function:
```
def test_parse_music__no_notes():
    music_string = ""
    result = parse_music(music_string)
    assert result == []

def test_parse_music__single_note():
    music_string = "o"
    result = parse_music(music_string)
    assert result == [4]

def test_parse_music__series_of_notes():
    music_string = "o o| o|.| o o|.|"
    result = parse_music(music_string)
    assert result == [4, 2, 1, 4, 2, 1]

def test_parse_music_multi_spaces():
    music_string = " o   o|   o|.| o   o|.|"
    result = parse_music(music_string)
    assert result == [4, 2, 1, 4, 2, 1]

def test_parse_music_non_matching_characters():