from typing import List


def sort_numbers(numbers: str) -> str:
    
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))




def test():
    assert sort_numbers('zero nine five three') == 'zero three five nine'
    assert sort_numbers('four seven two five zero') == 'zero two four five seven'
    assert sort_numbers('one zero six two eight four') == 'zero one two four six eight'
