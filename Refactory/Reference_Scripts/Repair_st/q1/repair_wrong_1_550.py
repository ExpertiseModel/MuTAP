def search ( x , seq ) :
    if ( seq is ( ) ) :
        return 0
    for ( i , elem ) in enumerate ( seq ) :
        if ( x <= elem ) :
            return i
    return len ( seq )
