def remove_extras ( lst ) :
    ref_lst_new = [ ]
    for ref_i in range ( len ( lst ) ) :
        if ( lst [ ref_i ] in ref_lst_new ) :
            continue
        else :
            ref_lst_new . append ( lst [ ref_i ] )
    return ref_lst_new
