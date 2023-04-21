def search ( x , seq ) :
    for i in range ( len ( seq ) ) :
        if ( x <= seq [ i ] ) :
            return seq . index ( seq [ i ] )
        elif ( x > seq [ ( - 1 ) ] ) :
            return ( seq . index ( seq [ ( - 1 ) ] ) + 1 )
    return 0
