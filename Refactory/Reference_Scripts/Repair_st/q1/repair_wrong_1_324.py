def search ( x , seq ) :
    for ( i , elem ) in enumerate ( seq ) :
        if ( seq == ( ) ) :
            return 0
        if ( x <= elem ) :
            return i
        elif ( x > max ( seq ) ) :
            return len ( seq )
    return len ( seq )
