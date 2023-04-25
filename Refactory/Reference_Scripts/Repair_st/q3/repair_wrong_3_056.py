def remove_extras ( new_lst ) :
    ref_new_lst = [ ]
    for i in new_lst :
        if ( i not in ref_new_lst ) :
            ref_new_lst += [ i ]
    return ref_new_lst
    pass
