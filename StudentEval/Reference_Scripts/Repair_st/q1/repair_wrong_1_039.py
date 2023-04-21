def search ( x , seq ) :
    ref_position = 0
    for i in range ( len ( seq ) ) :
        if ( x > seq [ i ] ) :
            ref_position = ( i + 1 )
        elif ( seq [ ( i - 1 ) ] < x < seq [ i ] ) :
            counter = i
    return ref_position
