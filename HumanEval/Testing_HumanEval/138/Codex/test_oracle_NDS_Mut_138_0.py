def is_equal_to_sum_even(n):
    
    return n%2 == 0 and n >= 8



def test():
    (
        lambda:
        TestCase.assertEqual(
            is_equal_to_sum_even(1), False
        )
    )()
    TestCase.assertEqual(
        is_equal_to_sum_even(1), False
    )
