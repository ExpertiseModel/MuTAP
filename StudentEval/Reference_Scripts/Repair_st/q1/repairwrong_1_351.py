def search ( x , seq ) :
    for ( i , p ) in enumerate ( seq ) :
        if ( x <= p ) :
            return i
    return len ( seq )
