def search ( x , seq ) :
    ref_index = 0
    for i in range ( len ( seq ) ) :
        if ( x <= seq [ i ] ) :
            a = i
            break
        elif ( x > seq [ i ] ) :
            ref_index = ( i + 1 )
    return ref_index
