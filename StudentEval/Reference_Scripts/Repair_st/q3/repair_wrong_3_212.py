def remove_extras ( lst ) :
    if ( lst == [ ] ) :
        return [ ]
    new_lst = [ lst [ 0 ] ]
    for i in range ( len ( lst ) ) :
        ref_a = lst [ i ]
        if False :
            pass
        pass
        for k in range ( i , len ( lst ) ) :
            pass
            if ( k == i ) :
                ref_ele = lst [ k ]
                if ( ref_ele in new_lst ) :
                    continue
                else :
                    pass
                new_lst . append ( ref_ele )
            pass
    return new_lst
