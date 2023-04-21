def search ( x , seq ) :
    if ( len ( seq ) == 0 ) :
        return len ( seq )
    else :
        for ( i , elem ) in enumerate ( seq ) :
            if ( elem >= x ) :
                return i
        return len ( seq )
