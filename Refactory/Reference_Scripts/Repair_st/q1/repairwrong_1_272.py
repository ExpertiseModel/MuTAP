def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    enumerated = list ( enumerate ( seq ) )
    if ( enumerated == [ ] ) :
        return len ( seq )
    else :
        for i in enumerated :
            if ( x <= i [ 1 ] ) :
                return i [ 0 ]
        return len ( seq )
