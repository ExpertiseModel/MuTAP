def remove_extras ( lst ) :
    new_lst = [ ]
    for ref_i in lst :
        if ( ref_i not in new_lst ) :
            new_lst += [ ref_i ]
    return new_lst
    pass
