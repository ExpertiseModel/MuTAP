def search ( x , seq ) :
    for ( i , elem ) in enumerate ( seq ) :
        if ( x == elem ) :
            return i
        elif ( x > elem ) :
            continue
        elif ( x < elem ) :
            return i
    return len ( seq )
