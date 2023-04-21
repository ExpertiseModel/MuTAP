def remove_extras ( lst ) :
    seq = [ ]
    for i in lst :
        if ( i not in seq ) :
            seq = ( seq + [ i ] )
    return seq
    pass
