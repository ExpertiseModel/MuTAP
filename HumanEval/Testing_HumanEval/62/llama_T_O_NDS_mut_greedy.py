def derivative(xs: list):
    
    return [(i * x) for i, x in enumerate(xs)][1:]


assert derivative([1, 2, 3, 4, 5]) == [2, 6, 12, 20]
