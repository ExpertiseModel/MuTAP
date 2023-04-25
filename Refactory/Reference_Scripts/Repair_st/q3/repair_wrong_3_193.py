def remove_extras ( lst ) :
    new_lst = lst . copy ( )
    new_lst . reverse ( )
    ori_len = len ( lst )
    rev_lst = lst . copy ( )
    for i in range ( ori_len ) :
        if ( new_lst [ i ] in new_lst [ ( i + 1 ) : ] ) :
            rev_lst . pop ( ( ( ori_len - i ) - 1 ) )
    return rev_lst
