def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    if True :
        pass
        for ( i , elem ) in enumerate ( seq ) :
            if ( elem < x ) :
                continue
            elif ( elem == x ) :
                return i
            elif ( elem > x ) :
                return i
        return len ( seq )
    pass
