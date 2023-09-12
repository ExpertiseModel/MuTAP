def match_parens(lst):
    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'Yes' if check(S1) or check(S2) else 'No'


# test case

def test():
    ## Test 1: Two strings with only '(' and ')'

    assert match_parens(['()', '()']) == 'Yes'

    ## Test 2: Two strings with '(' and ')' in different positions

    assert match_parens(['(())', '()']) == 'Yes'

    ## Test 3: Two strings with '(' and ')' in the same position

    assert match_parens(['( )', '()']) == 'No'


    ## Test 4: Two strings with nested '(' and ')'

    assert match_parens(['((()))', '((()))']) == 'Yes'


    ## Test 5: Two strings with conflicting '(' and ')'

    assert match_parens(['(()))', '()']) == 'No'


    ## Test 6: Two strings with varying number of '(' and ')'

    assert match_parens(['((()))', '()']) == 'Yes'


