def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

 # generate test case for the function above