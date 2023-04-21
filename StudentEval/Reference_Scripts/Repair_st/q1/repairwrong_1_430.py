def search ( x , seq ) :
    pass
    for ( i , elem ) in enumerate ( seq ) :
        pass
        if ( ( seq == ( ) ) or [ ] ) :
            return 0
        if ( elem == x ) :
            return i
        elif ( elem > x ) :
            return i
        pass
    return len ( seq )
