def search ( x , seq ) :
    for i in range ( 0 , ( len ( seq ) + 1 ) ) :
        if ( len ( seq ) == 0 ) :
            return 0
        elif ( x < seq [ i ] ) :
            return i
        elif ( seq [ i ] < x <= seq [ ( i + 1 ) ] ) :
            return ( i + 1 )
        elif ( x > seq [ ( len ( seq ) - 1 ) ] ) :
            return len ( seq )
