def search ( x , seq ) :
    n = len ( seq )
    for ( i , currentvalue ) in enumerate ( seq ) :
        if ( currentvalue < x ) :
            position = ( i + 1 )
        elif ( currentvalue == x ) :
            return position
        elif ( currentvalue > x ) :
            return i
    return len ( seq )
