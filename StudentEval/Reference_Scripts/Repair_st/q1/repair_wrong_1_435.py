def search ( x , seq ) :
    for ( i , elem ) in enumerate ( seq ) :
        if ( x <= elem ) :
            return i
        else :
            counter = len ( seq )
    return len ( seq )
