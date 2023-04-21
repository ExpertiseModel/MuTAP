def sum_to_n(n: int):
    
    return sum(range(n + 1))



def test():
    assert sum_to_n(3) == 6
    assert sum_to_n(10) == 55
    assert sum_to_n(100) == 5050

def main():
    test()

if __name__ == '__main__':
    main()
