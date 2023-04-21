def largest_divisor(n: int) -> int:
    
    for i in reversed(range(n)):
        if n % i == 0:
            return i



def test():
    assert largest_divisor(3) == 3, "3"
    assert largest_divisor(4) == 2, "2"
    assert largest_divisor(5) == 1, "5"
    assert largest_divisor(6) == 3, "3"
    assert largest_divisor(8) == 2, "4"
    assert largest_divisor(9) == 3, "3"
    assert largest_divisor(10) == 1, "5"
    assert largest_divisor(12) == 3, "3"
    assert largest_divisor(17) == 17, "17"
    assert largest_divisor(19) == 19, "19"
    assert largest_divisor(19) == 19, "19"


def main():
    test()
    print("Passed.")

main()
