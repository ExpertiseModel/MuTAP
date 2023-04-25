def remove_extras ( lst ) :
    lst = lst . copy ( )
    lst . reverse ( )
    ori_len = len ( lst )
    rev_lst = lst . copy ( )
    for i in range ( ori_len ) :
        if ( lst [ i ] in lst [ ( i + 1 ) : ] ) :
            rev_lst . pop ( ( ( ori_len - i ) - 1 ) )
    return rev_lst
