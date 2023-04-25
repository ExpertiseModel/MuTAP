def search ( x , seq ) :
    pass
    if ( ( seq == ( ) ) or ( seq == [ ] ) ) :
        return 0
    else :
        for ( i , elem ) in enumerate ( seq ) :
            pass
            if ( x <= seq [ i ] ) :
                return i
            elif ( x > seq [ ( len ( seq ) - 1 ) ] ) :
                return len ( seq )
            pass
        pass
