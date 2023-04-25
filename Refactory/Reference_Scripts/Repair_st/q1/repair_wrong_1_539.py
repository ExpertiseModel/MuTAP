def search ( x , seq ) :
    ref_index = 0
    for i in range ( len ( seq ) ) :
        if ( seq [ i ] >= x ) :
            break
        elif ( x > seq [ i ] ) :
            ref_index = ( i + 1 )
    return ref_index
