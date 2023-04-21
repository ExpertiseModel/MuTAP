def is_simple_power(x, n):
    
    if not (n == 1):
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 
