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
def test_empty_music():
    music = "   "
    assert parse_music(music) == []

def test_single_note():
    music = "o"
    assert parse_music(music) == [4]

def test_double_notes():
    music = "o|.|"
    assert parse_music(music) == [2, 1]

def test_multi_notes():
    music = ".o.|.o|"
    assert parse_music(music) == [1, 2, 4]

def test_mixed_notes():
    music = "o.o|.|"
    assert parse_music(music) == [2, 1, 4]

def test_whitespace():
    music = " \to.| "
    assert parse_music(music) == [1, 2, 4]

def test_empty_string():
    music = ""
    assert parse_music(music) == []

def