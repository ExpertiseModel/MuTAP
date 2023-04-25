def remove_extras ( new_lst ) :
    ref_new_lst = [ ]
    for i in new_lst :
        if ( i in ref_new_lst ) :
            continue
        else :
            ref_new_lst . append ( i )
        pass
    return ref_new_lst
