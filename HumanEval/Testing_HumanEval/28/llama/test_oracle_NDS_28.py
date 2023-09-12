from typing import List


def concatenate(strings: List[str]) -> str:
    
    return ''.join(strings)




# test case
def test():
    #test_empty_input
    concatenate([]) == ''

    #test_single_string
    concatenate(['hello']) == 'hello'

    #test_ multiple_strings
    concatenate(['hello', 'world', '!']) == 'hellogworld!'

    #test_list_with_none
    concatenate([None, 'hello', 'world']) == 'helloworld'

    #test_list_with_empty
    concatenate(['', 'hello', 'world']) == 'helloworld'

    #test_list_with_list
    concatenate([['hello'], ['world']]) == 'helloworld'

    #test_list_with_special
    concatenate(['hello', 'world', '@']) == 'hellogworld!'

    #test_list_with_unicode
    concatenate(['hello', 'world', u'\u0000']) == 'hellogworld!'

    #test_list_with_empty_list
    concatenate([]) == ''