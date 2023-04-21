def remove_extras ( lst ) :
    ref_rem_lst = [ ]
    for i in lst :
        if ( ref_rem_lst . count ( i ) == 0 ) :
            ref_rem_lst += [ i ]
    return ref_rem_lst
