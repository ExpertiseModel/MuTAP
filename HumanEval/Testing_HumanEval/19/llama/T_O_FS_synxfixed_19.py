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
   
    assert sort_numbers('') == ' '

    assert sort_numbers('2') == '2'

    assert sort_numbers('12') == '12'

    assert sort_numbers('256') == '256'

    assert sort_numbers('4321') == '4321'

    assert sort_numbers('90210') == '90210'

#</test case>
