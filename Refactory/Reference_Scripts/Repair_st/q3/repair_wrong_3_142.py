def remove_extras ( lst ) :
    pass
    if ( lst != [ ] ) :
        ref_my_list = [ ]
        for j in range ( len ( lst ) ) :
            pass
            if ( lst [ j ] not in ref_my_list ) :
                ref_my_list . append ( lst [ j ] )
            pass
        return ref_my_list
    else :
        return [ ]
    pass
