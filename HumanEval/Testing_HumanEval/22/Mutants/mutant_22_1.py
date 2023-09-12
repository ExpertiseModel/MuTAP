from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    
    return [x for x in values if not isinstance(x, int)]