def search ( x , seq ) :
    for ( i , elem ) in enumerate ( seq ) :
        if ( x <= elem ) :
            return i
        elif ( elem > x ) :
            return len ( seq )
    return len ( seq )
