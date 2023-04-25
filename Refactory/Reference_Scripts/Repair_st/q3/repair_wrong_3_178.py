def remove_extras ( lst ) :
    ref_new_lst = [ ]
    for i in range ( len ( lst ) ) :
        pass
        if ( lst [ i ] not in ref_new_lst ) :
            ref_new_lst . append ( lst [ i ] )
    return ref_new_lst
