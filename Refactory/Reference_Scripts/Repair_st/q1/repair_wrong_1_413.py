def search ( x , seq ) :
    pass
    for ( i , elem ) in enumerate ( seq ) :
        if ( x <= elem ) :
            return i
    return len ( seq )
