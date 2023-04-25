def remove_extras ( lst ) :
    ref_new = [ ]
    while ( lst != [ ] ) :
        ref_new = ( ref_new + [ lst [ 0 ] ] )
        ref_check = lst [ 0 ]
        i = 0
        while ( i < len ( lst ) ) :
            if ( lst [ i ] == ref_check ) :
                lst . remove ( lst [ i ] )
                i = i
            i = ( i + 1 )
    return ref_new
