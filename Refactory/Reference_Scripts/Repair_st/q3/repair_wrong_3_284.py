def remove_extras ( lst ) :
    ref_new_lst = [ ]
    for x in range ( len ( lst ) ) :
        if ( lst [ x ] not in ref_new_lst ) :
            ref_new_lst . append ( lst [ x ] )
    return ref_new_lst
