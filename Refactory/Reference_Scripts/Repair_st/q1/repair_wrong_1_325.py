def search ( x , seq ) :
    for ( i , elem ) in enumerate ( seq ) :
        if ( seq == ( ) ) :
            return None
        if ( x <= elem ) :
            return i
        elif ( x > max ( seq ) ) :
            return len ( seq )
    return len ( seq )
