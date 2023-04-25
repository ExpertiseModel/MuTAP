def search ( x , seq ) :
    def helper ( index ) :
        if ( not seq ) :
            return 0
        elif ( x <= seq [ index ] ) :
            return index
        elif ( ( index + 1 ) >= len ( seq ) ) :
            return ( index + 1 )
        else :
            return helper ( ( index + 1 ) )
    return helper ( index )
